#!/bin/sh

scrapy crawl match_url_spider
scrapy crawl soccer_spider
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/PreCleanData.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/BreakReports.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python Metrics.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/PandNSeperation.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/SeperatedDataGetMetrics.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python CSVFilesToReport.py
cp -b ./metrics/metrics_seperared.csv ./metrics/top10CommonNegativeWordsFrequency.png ./metrics/top10CommonNegativeWordsTFIDF.png metrics/top10CommonPositiveWordsFrequency.png ./metrics/top10CommonPositiveWordsTFIDF.png metrics/top10NegativeWordsCount.png metrics/top10PositiveWordsCount.png  ./Document
pdflatex /Document/report.tex