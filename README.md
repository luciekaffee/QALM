# QALM Dataset

QALM provides a dataset for multilingual question answering over a set of different popular knolwedge graphs extending the [QALD-9 dataset](https://2018.nliwod.org/challenge).
The knowledge graphs covered are:
* Wikidata
* DBpedia 
* YAGO
* MusicBrainz
* LinkedMDB

QALD (and therefore QALM) covers a set of languages, in QALM we use the following languages:
* English
* Spanish
* Hindi

As the original dataset (QALD) provides more languages, more languages can be mapped to QALM by using the question ID and map the questions to the original [QALD (training) dataset](https://github.com/ag-sc/QALD/blob/master/9/data/qald-9-train-multilingual.json).

We provide answers for all questions as retrieved by the knowledge graphs at the time as well as their classes as we needed those for our approach in [LINGVO](https://github.com/luciekaffee/LINGVO).
The answers are provided as labels in the three languages, the classes as URIs.

All data can be found in the [QALM dataset file](QALM.json).


## Citation

To cite this work please use:
```tex
@inproceedings{DBLP:conf/kcap/KaffeeESV19,
  title     = {Ranking Knowledge Graphs By Capturing Knowledge about Languages and
               Labels},
  author    = {Lucie{-}Aim{\'{e}}e Kaffee and
               Kemele M. Endris and
               Elena Simperl and
               Maria{-}Esther Vidal},
  booktitle = {Proceedings of the 10th International Conference on Knowledge Capture,
               {K-CAP} 2019, Marina Del Rey, CA, USA, November 19-21, 2019},
  publisher = {{ACM}},
  year      = {2019},
  url       = {https://doi.org/10.1145/3360901.3364443}
```


## License

QALM is MIT licensed, as found in the [LICENSE.txt](LICENSE.txt) file.