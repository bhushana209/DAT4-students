I've just now almost been able to extract the necessary data from the USPTO patent grant xmls. For the 145 weeks of patent grant data contained in the xmls, I've been able to extract the following:
+ 806,485 rows of data containing:

	+ Patent Grant No.
	+ Invention Title
	+ Kind of patent granted
	+ Date of patent grant
	+ Application type
	+ Date of application
	+ Main USG classification of patent
	+ Number of references cited in the patent
	+ The name, city, state, and country of the patent holder(s)
	+ The name(s) of the people who applied for the patent and the number of them
	+ The patent's abstract (where available)
	+ The claims made in the patent

The patent types break down as:
|utility  |  739535 |
|design   |  62339  |
|plant    |  2491   |
|reissue  |  2092   |
|sir      |  28     |

There are 72,620 different main classifications.

There are 105,468 different patent holder organizations in 29,017 different cities, 58 states (including 'None'), and 155 different countries. I know this data needs a lot of cleaning: cities and companies contain multiple different entries describing the same thing, sometimes there are multiple patent holders in different locations, etc.

The breakdown of how many references are cited in patents are as follows:

|count  |  806485.000000 |
|mean   |      14.572965 |
|std    |      66.595555 |
|min    |       0.000000 |
|25%    |       0.000000 |
|50%    |       0.000000 |
|75%    |      10.000000 |
|max    |    3493.000000 |

I initially thought that the max value was a mistake of some kind, but looking at the data, it seems that it's legit. The 5 highest numbers of references cited all belong to Abbot Industries and have to do with diabetes treatment.

The breakdown of the number of applicants per patent is:

|count  |  806485.000000 |
|mean   |       0.904539 |
|std    |       1.671731 |
|min    |       0.000000 |
|25%    |       0.000000 |
|50%    |       0.000000 |
|75%    |       1.000000 |
|max    |      38.000000 |

Other than that, I haven't gotten terribly far.

Things I still need to do:

+ Clean the patent data
+ Use the cleaned patent holder names with the Crunchbase api available on [Mashape](https://www.mashape.com/community/crunchbase) to identify the overlap and get the funding rounds, amounts, and funding institution names.
+ I'd like to do text analysis on the claims and/or abstracts to see if there's any correlation with those and funding. Hopefully I'll get that far.




