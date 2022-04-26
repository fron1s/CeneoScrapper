# CeneoScraper

## Single  opinion structure

|Element|Selector|Variable|
|-------|--------|--------|
|Opinion|div.js_product-review|opinion|
|Opinion id|\["data-entry-id"\]|opinion_id|
|Author|span.user-post__author-name|author|
|Recommendation|span.user-post__author-recomendation > em|rcmd|
|Stars score|span.user-post__score-count|score|
|Content|div.user-post__text|content|
|List of adventages|div.review-feature__title--positives  ~ div.review-feature__item|pros|
|List of disadventages|div.review-feature__title--negatives  ~ div.review-feature__item|cons|
|Date of posting opinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\]|bought_on|
|For how many users useful|button.vote-yes > span|useful_for|
|For how many users useless|button.vote-no > span|useless_for|

## Stages of project

1) Extraction of elements for a single opinion to separate variables
2) Extraction of elements for a single opinion to one complex variable
3) Extraction of all opinions from single page to list
4) Extraction of all opinions for certain product  and saving it to a file