#import "@local/typst-templates:0.1.0": general_template
#show: general_template.with(
  title: "Research Paper -- Writing And Statistics",
  prefix: [_AP Research & Senior Research Project_],
  authors: none,
  suffix: [#link("https://github.com/ojas-chaturvedi")],
  enable-footer: true,
)

Last week, I finished generating my results and creating graphs for an analysis of my results. However, while the analysis of the graphs had some interesting results, the main question of the project still wasn't answered: To what extent do the sentiments expressed in pro-control versus pro-rights congressional gun legislation differ?

To understand how the legislation sentiments differ, a statistics test must be implemented to compare the sentiments of pro-control and pro-rights legislation together. A T-test was chosen as it would help determine if there is a significant difference between the means of the 2 sides and how they are related. Specifically, I will be conducting a 2 independent sample T-test, as I go in with the assumption that the sentiments of the sides are independent and have no effect on each other.

However, the specific version of the test will depend on whether the distribution of both samples follows the normal, or Gaussian, distribution. What this means is that the majority of sentiment scores will be close to the mean (average) score, and the overall distribution of sentiment scores will be symmetric around the mean. Additionally, the extreme values (both highly positive and highly negative sentiments) are less common and represent outlier sentiments that are not typical of the overall set of legislation. To calculate whether a distribution is normal, a Shapiro-Wilk test can be conducted to prove if the samples fit a normal distribution. With a Shapiro-Wilk test, the null hypothesis, which we can either reject or fail to reject, is that the set of data comes from a normal distribution. If the null hypothesis is rejected, the alternative hypothesis, which is that the set of data does not come from a normal distribution, is accepted.

If both samples follow a normal distribution, an Independent Samples T-test will be conducted. If not, then a Mann-Whitney U test will be conducted. With both tests, the null hypothesis is always that there is no significant difference between both samples. Therefore, the null hypothesis would be that there is no difference (in terms of central tendency) in sentiments between pro-control and pro-rights congressional gun legislation. The alternative hypothesis is that there is a difference (in terms of central tendency) in sentiments between pro-control and pro-rights congressional gun legislation.

These tests will be conducted the following weekend and then be added to my research paper. The progress on my research paper has been very substantial, having finished the Introduction/Literature Review, Methodology, and Results/Analysis sections. The 2 sections of the paper I have left are the Discussion section, which will include a summary of the analysis, implications of my research project, and some limitations that influenced my understanding, as well as the Conclusion section, which will give a quick summary of the research paper. I aim to have this research paper finished by Monday 4/29 to be submitted to CollegeBoard and BASIS Chandler. My presentation for this project is tomorrow, Saturday 4/27, but I have already finished my PowerPoint slides and presented my findings for AP Research, so presenting for the Senior Research project shouldn't be different.
