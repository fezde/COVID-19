---
title: Definitions
type: page
sorter: 70
---

## Basic numbers

This section contains only definitions for numbers that are directly loaded (or received) from data sources. No additional calculation is done.

* **Population (`P`)**: Source google.com. E.g. [Population of Germany](https://www.google.com/search?source=hp&ei=OuCIXs-jL8_JkwXA4I74CA&q=population+germany&oq=Populatino+Germ&gs_lcp=CgZwc3ktYWIQAxgAMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgYIABANEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoFCAAQgwE6AggAOgcIABBGEPkBOgQIABAKOgkIABANEEYQ-QE6BggAEA0QCkooCBcSJDBnOTZnNzhnODNnMTExZzgxZzk2ZzgyZzg2Zzk2ZzEwMWc5OUobCBgSFzBnMWcxZzFnMWcxZzFnMWcxZzFnNWcxUO8dWJ02YNY_aABwAHgAgAFoiAHACpIBBDEzLjKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab)
* **Confirmed (`C`)** the number of confirmed cases of a COVID-19 infection. [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
* **Deaths (`D`)**: the number of deaths. [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
* **Recovered (`R`)**: the number of recovered cases. [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

## Derived numbers

This section defineds a set of derived measures.

* **Case fatality rate (`CFR := D/C`)** is the proportion of deaths from a certain disease compared to the total number of people diagnosed with the disease for a certain period of time. [Wikipedia](https://en.wikipedia.org/wiki/Case_fatality_rate)
* **Case survival rate (`CFR := R/C`)** is the proportion of recoveries from a certain disease compared to the total number of people diagnosed with the disease for a certain period of time.
* **Ill People (`IP := C - D - R`)** is the number of people who are still ill with COVID-19.
* **Ill People Rate (`IPR := IP/P`)** is the number of people of a given country, who are still ill with COVID-19, compared to the total population of that country.
* **Infection Rate (`IR := C/P`)** is the probability or risk of an infection in a population. [Wikipedia](https://en.wikipedia.org/wiki/Infection_rate)
* **Mortality Rate (`MR := D/P`)** is a measure of the number of deaths (in general, or due to a specific cause) in a particular population, scaled to the size of that population [Wikipedia](https://en.wikipedia.org/wiki/Mortality_rate)
* **Recovery Rate (`RR := R/P`)** is the proportion of recoveries from a certain disease compared to the size of a particular population.
