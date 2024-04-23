#import "@preview/charged-ieee:0.1.0": ieee

#show: ieee.with(
  title: [
    Legislative Narratives on Gun Control in the United States: A Sentiment Analysis Approach
  ],
  // abstract: [
  //   ABSTRACT GOES HERE
  // ],
  // authors: ((
  //   name: "Ojas Chaturvedi",
  //   department: [Student],
  //   organization: [BASIS Chandler],
  //   location: [Chandler, Arizona],
  //   email: "oj.chaturvedi.2024@gmail.com",
  // ),),
  // index-terms: (
  //   "Natural Language Processing",
  //   "Sentiment Analysis",
  //   "Gun Control",
  //   "VADER",
  //   "Large Language Models",
  // ),
  bibliography: bibliography("refs.bib"),
)

= Introduction & Literature Review
_(Introduces the research question, reviews previous work in the field, and presents a gap in the field)_

= Methodology
_(Provides an explanation of and justification for the chosen method or process)_

== Data Collection
As this study focuses on congressional legislation, all legislative data was sourced from Congress.gov, the official website for legislative information. Using the advanced search function with specific search terms and filters, I was able to identify the legislation relevant to the gun control debate. The search term “gun” and the legislation category option were used to capture a comprehensive list of relevant legislation. To further refine my search, I specified a timeframe spanning congressional sessions 101-117 (January 3rd, 1989, to January 3rd, 2023). The starting point of 1989 was chosen because legislation text prior to this session is unavailable, while the ending point in 2023 reflects the ongoing nature of the 118th congressional session, which has not yet concluded and continues to generate new legislative content. Lastly, the status of legislation was set to all options, including failed legislation, as although unsuccessful legislation lacks real-world impact, its value lies in understanding legislators' framing of issues. Even failed legislation can be beneficial as it provides additional insights from legislators. 

After conducting the search, I then used the bulk download feature to extract relevant data on each piece of legislation. Using this option, I received the Legislation Number, URL, Congressional Session, Title, Party of Sponsors, and Date of Introduction of each legislation, all of which have a purpose in this study. The Legislation Number serves as a unique identifier, differentiating each piece of legislation and providing information on its origin, including the chamber in which it was introduced and the type of legislation. The URL is used later on as part of a web scraper to gather the text for each piece of legislation. The Date of Introduction is used later on in the analysis to determine how legislation sentiment changes over time, while the Party of Sponsors will be used to determine the side (pro-control or pro-rights) each political party is on. 

While the bulk download feature provides much useful information, it does not provide the actual legislative text to conduct the sentiment analysis. Therefore, I created a web scraper to use the URLs from the bulk download to retrieve the textual data. Using the Selenium Python library, I simulated a Google Chrome browser to open a modified URL link that points directly to the website with the legislative link and retrieve the HTML source code, which contains all the elements of the website including the text. I then parsed the HTML code to extract the relevant legislation text using the BeautifulSoup4 Python library. Before saving the text in a CSV file with all of the other information from the bulk download feature on Congress.gov, I created a script to pre-process the text to prepare it for sentiment analysis. The script finds and removes the header and signatories' information before the actual legislation text. Next, the script conducts a series of pre-processing methods as detailed in @7862202. This involves replacing grammatical contractions with their expanded forms, removing URL links, removing numbers, expanding acronyms to their full form, and removing stop words. Stop words, including “the”, “is”, and “at”, are words that are very common and have no sentiment, which is why they are removed before the sentiment analysis step. The stop words removed from the script were taken from @fox_stop_nodate. With the text pre-processed, it is saved and ready for its classification and sentiment analysis.

= Results / Findings
_(Presents findings or results)_

= Discussion / Analysis
_(Interprets the significance of results in the context of the research question)_

= Conclusion & Future Directions
_(Highlights a new understanding, the limitations of your methodology, possible implications of your project, and future research that could be accomplished)_

= Reference List
