#!/bin/sh

scrapy crawl match_url_spider
scrapy crawl soccer_spider
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/PreCleanData.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/BreakReports.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python Metrics.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/PandNSeperation.py
/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/env/bin/python /home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/SeperatedDataGetMetrics.py
pdflatex /Document/report.tex