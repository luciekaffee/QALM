import json

questions = json.load(open('../data/all-qald-questions.json'))

answers_tmp = json.load(open('../data/all-query-results.json'))
answers = {}
for lang, data in answers_tmp.iteritems():
    for kg, v in data.iteritems():
        for qid, val in v.iteritems():
            if not qid in answers:
                answers[qid] = {}
            if not kg in answers[qid]:
                answers[qid][kg] = {}
            if not lang in answers[qid][kg]:
                answers[qid][kg] = {}
            answers[qid][kg][lang] = val

queries = {}

with open('../data/Query-translation.tsv') as infile:
    next(infile)
    for line in infile:
        tmp = line.split('\t')
        queries[tmp[0].strip()] = {}
        if not tmp[2] or tmp[2].lower().strip() == 'x':
            queries[tmp[0].strip()]['dbpedia'] = []
        else:
            queries[tmp[0].strip()]['dbpedia'] = tmp[2].strip()
        if not tmp[3] or tmp[3].lower().strip() == 'x':
            queries[tmp[0].strip()]['musicbrainz'] = []
        else:
            queries[tmp[0].strip()]['musicbrainz'] = tmp[3].strip()
        if not tmp[4] or tmp[4].lower().strip() == 'x':
            queries[tmp[0].strip()]['wikidata'] = []
        else:
            queries[tmp[0].strip()]['wikidata'] = tmp[4].strip()
        if not tmp[5] or tmp[5].lower().strip() == 'x':
            queries[tmp[0].strip()]['yago'] = []
        else:
            queries[tmp[0].strip()]['yago'] = tmp[5].strip()
        if not tmp[6] or tmp[6].lower().strip() == 'x':
            queries[tmp[0].strip()]['linkedmdb'] = []
        else:
            queries[tmp[0].strip()]['linkedmdb'] = tmp[6].strip()

def replace_names(crowd):
    crowd_res = {}
    for k,v in crowd.iteritems():
        if v == 'yg':
            crowd_res[k] = 'yago'
        elif v == 'wd':
            crowd_res[k] = 'wikidata'
        elif v == 'db':
            crowd_res[k] = 'dbpedia'
        elif v == 'mb':
            crowd_res[k] = 'musicbrainz'
        elif v == 'linked':
            crowd_res[k] = 'linkedmdb'
        else:
            print 'ERROR: new name in crowd evaluation!' + str(v)
            crowd_res[k] = v
    return crowd_res

crowd_en = replace_names(json.load(open('../data/crowd-en.json')))
crowd_es = replace_names(json.load(open('../data/crowd-es.json')))
crowd_hi = replace_names(json.load(open('../data/crowd-hi.json')))

domains = {}
with open('../data/Domains.tsv') as infile:
    next(infile)
    for line in infile:
        tmp = line.split('\t')
        domains[tmp[0].strip()] = tmp[2].replace('\n', ' ').strip()

classes_tmp = json.load(open('../data/classes.json'))

classes = {}
for kg, data in classes_tmp.iteritems():
    for qid, val in data.iteritems():
        if not qid in classes:
            classes[qid] = {}
        if not kg in classes[qid]:
            classes[qid][kg] = {}
        if not lang in classes[qid][kg]:
            classes[qid][kg] = {}
        classes[qid][kg][lang] = val

dataset = {}
for qid, qs in questions.iteritems():
    if not qid in queries:
        continue
    dataset[qid] = {}
    dataset[qid]['questions'] = qs
    dataset[qid]['queries'] = queries[qid]
    dataset[qid]['answers'] = answers[qid]
    dataset[qid]['domain'] = domains[qid]
    dataset[qid]['classes'] = classes[qid]
    if qid in crowd_en:
        dataset[qid]['crowd_en'] = crowd_en[qid]
    else:
        dataset[qid]['crowd_en'] = []
    if qid in crowd_hi:
        dataset[qid]['crowd_hi'] = crowd_hi[qid]
    else:
        dataset[qid]['crowd_hi'] = []
    if qid in crowd_es:
        dataset[qid]['crowd_es'] = crowd_es[qid]
    else:
        dataset[qid]['crowd_es'] = []

print 'generated dataset'
json.dump(dataset, open('../QALM.json', 'w'))