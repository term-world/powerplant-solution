| Date              |          |
|:------------------|:---------|
| Todo | Assigned |
| Todo | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# KEEPING UP WITH CURRENT EVENTS, POLITICIAN PROPOSES POWER PRODUCTION FOR PLAUDITS

**Reported by `Official Mayor-Endorsed News` on `Todo`**

If you thought surveillance was a shocking trick, the Mayor's Office is all charged up about a new effort: sidelining the environment to feed the new manufacturing craze in `term-world`. As the Mayor commented during a recent presss conference, he's apparently "not the only one who's power hungry around here."

Until now, citizens haven't taken advantage of the digital riches in coal, oil, and, well renewables like solar and wind power (we guess, if you're into that) and the energizing effect they could have on the `term-world` economy. Forget about nature versus nuture, the new calling card is _nature versus neutrons_.

Each neighborhood is being asked to work together to provide a model for what electrification looks like in the world. What path will provide the charge for the future? Giga-what neighborhood will emerge as new luminaries? How will we continue to power hearth and ohm?

## Overview

In this activity, you'll:

* discover how to import custom modules and use them as `object`s
* continue to create `class`es and `object`s to achieve purpose-built tasks
* observe strange, but productive, `object` behaviors
* begin to explore the concept of `object` `inheritance`, a way to "template" mulitple objects at once

### Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the Readme might be taken out.

## Completing `powerplant` content

For our final regular activity, we have some decisions to make: some about design and some about more-or-less environmentally-friendly options. This task is all about choices. 

Here's a list of broad goals, some of which we'll complete together:

* survey the array of fuel options and how to do use each
* charge a `.battery` file, logging how much each energy source generates
* design ways to generate power that leverage the strenghts of the sources to generate the most power
* pursue all of these goals to win a coveted prize for generating the most energy

### Energy sources

`term-world` boasts a mix of `Oil`, `Coal`, `Wind`, and `Solar` power options, available as part of the `resources` module.

|Type |Exhaustion |Energy yield |Amount yielded |
|:----|:----------|:------------|:--------------|
|`Oil`|Exhaustible|1667 kWh per barrel |5 barrels |
|`Coal`|Exhaustible|5549 kWh per short ton|2 short tons|
|`Solar`|Inexhaustible|1.2% panel wattage per second |1 second |
|`Wind`|Inexhaustible |Various, depending on `blade_size`†, wind speed |1 second |

`†` Maximum blade size is `115` meters; the larger the blade size, the slower the speed

#### Properties and methods of each source (by category)

##### Exhaustibles

Each exhaustible should use:

* an `energy` _property_ to store energy generated
* a `use` method to access the energy in the resource tapped

##### Inexhaustibles

###### `WindFarm`

* a `blade_size` property to set the size of the turbine blade
* a `super().__init__()` call to access properties and methods of the `Wind`

###### `SolarField`

* a `wattage` property to set the maximum wattage of the solar panel
* a `super().__init__()` call to access properties and methods of `Solar` energy

#### Note about `Exhaustibility`

##### Exhaustibles

Anything marked `Exhaustible` has a finite limit. At some point, the world runs out. It could happen now, it could happen in a year (or century). We simply don't know.

##### Inexhaustibles

While true that these sources do not have a limit, they can only be "harvested" during the right conditions (i.e. a wind greater than `5` mph or on sunny days that the sun is _actually_ showing). The `term-world` news page is a great source for this information. 

To call up the news page, use `CTRL + SHIFT + P` and type `menu` to filter the results. `term-world Menu: Show` should appear as an option.

### `reflection.md`

Don't forget to finish the `reflection.md` file in the `paperwork` folder!

## Improvement suggestions

Here are some suggestions for improvements you can, **but are not limited to** use:

|Improvement Suggestions |Description        |
|:-----------------------|:------------------|
|Objects            |Create an object that uses stored power |
|Objects            |Create an object hooked up directly to a power source |
|Conditional statements |Create an interface to choose power sources to use |
|Iteration          |Automate power generation based on time, demand, or other reason |
|Data visualization           |Create a dashboard (using `rich`) to visualize the contents of the `.battery`|
|Data structures/Objects    |Display the weather conditions underlying the renewable sources†|
|Objects            |Find and use the secret power source† |
|Data visualization |Create a poster about the `term-world` Energy Development and Industrial Utility Management supply chain |

`†` _Probably_ uses the `dir()` function to begin to explore `object`s

**Make sure to link your issue with the pull request you used to make your actually improvement.**

**If you are not following an improvement suggestion you need to have your improvement suggestion checked by the professor before proceeding.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.