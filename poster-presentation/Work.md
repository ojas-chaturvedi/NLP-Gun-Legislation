# Work

- [Work](#work)
  - [Project Title](#project-title)
  - [Research Question](#research-question)
  - [Hypothesis](#hypothesis)
  - [Background / Context](#background--context)
    - [Contextualizing the Gun Control Debate](#contextualizing-the-gun-control-debate)
    - [Rationale for Using Sentiment Analysis](#rationale-for-using-sentiment-analysis)
  - [Definitions](#definitions)
  - [Assumptions](#assumptions)
  - [Significance / Importance of Study](#significance--importance-of-study)
  - [Method of Inquiry](#method-of-inquiry)
    - [Data Collection](#data-collection)
    - [Data Preprocessing](#data-preprocessing)
    - [Linguistic Landscape Modeling (LLM)](#linguistic-landscape-modeling-llm)
    - [Sentiment Analysis](#sentiment-analysis)
    - [Data Visualization and Analysis](#data-visualization-and-analysis)
    - [Iterative Analysis](#iterative-analysis)
    - [Ethical Considerations](#ethical-considerations)
  - [Key Sources](#key-sources)


## Project Title

Shooting Through the Text: Uncovering Sentiments in Congressional Gun Legislation

## Research Question

What insights can a multi-model sentiment analysis reveal about the framing of legislation containing the word 'gun' introduced in the U.S. Congress between the 107th and 118th sessions (2001-2024)?

## Hypothesis

The sentiment analysis of U.S. Congressional bills containing the term 'gun' from the 107th to 118th sessions demonstrates a clear trend of increasing polarization in legislative language. This analysis indicates that over time, bills have increasingly adopted more definitive stances, either strongly favoring gun control measures or advocating for gun rights, mirroring the deepening societal and political divide on gun-related issues.

## Background / Context

### Contextualizing the Gun Control Debate

**Historical and Contemporary Landscape**: The gun control debate in the United States has deep historical roots, tracing back to the Second Amendment. This debate has intensified, especially in light of events like the Sandy Hook and Parkland shootings, which have spurred legislative actions at both federal and state levels. Advocates on both sides, pro-gun and pro-control, present starkly contrasting views, reflecting the nation's divided stance.

**Public Opinion and Policy**: Public opinion on gun-related issues, often measured through surveys and reflected in media coverage, has shown significant variation and intensity. This fluctuating public sentiment influences political discourse and shapes legislative priorities, demonstrating a complex interplay between societal attitudes, political ideologies, and policy-making.

**Legislative Responses and Diversity**: In response to these debates, the U.S. Congress has introduced a broad spectrum of bills concerning gun regulation and rights. This legislative diversity is seen in measures ranging from the proposed Assault Weapons Ban to laws expanding concealed carry rights, reflecting the evolving stance on gun-related matters across the nation.

### Rationale for Using Sentiment Analysis

**Advancing Beyond Traditional Analysis**: While traditional legislative analysis focuses on legal and policy aspects of bills, it often overlooks the emotional and psychological dimensions. The integration of sentiment analysis permits a deeper exploration of the emotional tone and rhetorical strategies embedded in legislative language, thus providing a more holistic understanding of these bills.

**Technological Innovations in Analyzing Legislative Text**: The advancements in Natural Language Processing, including tools like text mining and machine learning algorithms, offer innovative methods to dissect the nuances in legislative bills. This approach can unearth underlying sentiments and framing strategies, offering insights into how legislators craft their message on gun-related issues.

**Filling the Research Gap in Legislative Analysis**: Despite its wide application in various fields, sentiment analysis remains relatively unexplored in the realm of gun control legislation. This project seeks to bridge this gap, aiming to shed light on the linguistic patterns and emotional undertones in gun control bills and how these may reflect broader societal and political sentiments. The findings have the potential to inform future legislative drafting and political strategy, contributing to a more nuanced understanding of this pivotal issue.

## Definitions

**Gun Control**: Refers to any regulation related to the manufacture, sale, transfer, possession, modification, or use of firearms.

**Second Amendment**: A part of the U.S. Constitution that safeguards the right to keep and bear arms, frequently at the core of the gun control debate.

**Legislative Bill**: A formal proposal for new legislation, presented for consideration and debate within a legislative body.

**Rhetorical Strategies**: Techniques used in arguments to influence audiences, often through appeals to emotion, logic, or credibility.

**Sentiment Analysis**: A computational process that identifies and categorizes opinions in text, aiming to ascertain the writer's attitude towards a specific topic.

**Natural Language Processing (NLP)**: An area of artificial intelligence that enables computers to understand, interpret, and manipulate human language, bridging human communication and computer understanding.

## Assumptions

**Consistency in Legislative Language**: The analysis assumes that the language used in legislative bills is consistent and structured enough to allow for accurate sentiment analysis. This includes the assumption that the language is sufficiently clear and unambiguous to be interpreted by sentiment analysis algorithms.

**Reliability and Neutrality of Analysis Tools and Process**: The project assumes the sentiment analysis tools and NLP techniques are both effective in interpreting legislative language nuances and inherently neutral, ensuring an unbiased, accurate capture of emotional tones and rhetorical strategies.

**Interplay of Societal Attitudes and External Events**: This project posits a complex relationship between stable societal attitudes and the influence of external events on legislative language, with sentiment analysis expected to detect these nuanced influences over the analyzed periods.

**Representativeness and Generalizability of Legislative Analysis**: It is assumed that the selected bills for analysis accurately reflect broader legislative trends in gun control from the 107th to 118th Congress sessions, allowing for generalization of the findings to broader federal legislative trends.

## Significance / Importance of Study

This study holds paramount significance within the realm of legislative analysis, particularly in the intricate landscape of gun control. Its pioneering use of sentiment analysis to unravel the emotional and rhetorical dimensions of legislative bills fills a critical void in the field. Traditionally, legislative analysis has predominantly focused on the legal and policy aspects of bills, often overlooking the emotional underpinnings that significantly shape legislative language. By embracing sentiment analysis, this study delves into uncharted territory, shedding light on the nuanced sentiments embedded within gun control bills.

The value of this study is multi-fold. Firstly, it enriches our comprehension of legislative rhetoric, providing a holistic understanding of how emotions and rhetorical strategies permeate these critical documents. By uncovering the emotional tones, persuasive techniques, and framing strategies employed by legislators, it offers a deeper insight into how lawmakers convey their messages on the contentious issue of gun control. This knowledge is invaluable for policymakers, who can make more informed decisions by considering not just the legal text but also the emotional tenor of proposed bills.

Secondly, this research benefits legal practitioners by providing a novel tool for crafting persuasive arguments. By tapping into the insights gained from sentiment analysis, attorneys can strategically navigate the emotional landscape of gun control legislation, enhancing their ability to advocate effectively in the legal arena.

Furthermore, this study serves as a pioneering example of how sentiment analysis, powered by advanced Natural Language Processing techniques, can be applied to legislative analysis. It extends the boundaries of sentiment analysis, showcasing its versatility in unraveling the subtle nuances of legal texts. This methodology sets a precedent for future studies, not only in the domain of gun control but across various legislative topics. It opens up new avenues for research, promising a deeper understanding of legislative language and sentiment in an era where data-driven approaches are becoming increasingly essential.

In conclusion, the significance and importance of this study lie in its innovative approach to understanding the emotional dimensions of gun control legislation, bridging a substantial gap in legislative analysis. It offers practical insights for policymakers and legal practitioners, while also contributing to the broader academic discourse by advancing the application of sentiment analysis in the legislative domain. This endeavor has the potential to shape not only how we perceive legislative language but also how we engage in discussions and decisions on one of the most contentious issues in contemporary society.

## Method of Inquiry

### Data Collection

The first step in our methodology involves harnessing the power of the Playwright web automation library in conjunction with the GovTrack.US API. This combined approach allows us to gather comprehensive data on congressional gun legislation introduced in the U.S. Congress during the 107th to 118th sessions. The data is meticulously collected and structured in JSON format, ensuring that we capture a detailed snapshot of legislative activities during the specified time frame.

### Data Preprocessing

Following data collection, a crucial preprocessing step is employed to refine the dataset. This step serves the dual purpose of enhancing data quality and mitigating potential ethical concerns. Data points that might raise ethical issues or distort the analysis are systematically removed, ensuring that our subsequent analysis remains ethically sound and methodologically robust.

### Linguistic Landscape Modeling (LLM)

With the curated dataset in hand, we turn to Linguistic Landscape Modeling (LLM) to categorize the gathered gun legislation. LLM, a state-of-the-art approach in Natural Language Processing, enables us to extract meaningful insights by analyzing the textual content of bills. Through this categorization, we gain a comprehensive understanding of the legislative landscape, allowing for a nuanced sentiment analysis.

### Sentiment Analysis

The heart of our methodology lies in the sentiment analysis of the categorized gun legislation. Leveraging advanced sentiment analysis techniques, we dissect the emotional tone, rhetorical strategies, and sentiment of each legislative document. This step unveils the emotional undercurrents that often remain concealed in traditional legislative analysis, providing a profound insight into the language and sentiments embedded in the bills.

### Data Visualization and Analysis

To complement our sentiment analysis, we employ cutting-edge graph libraries and data visualization tools. These tools enable us to craft compelling visual representations of the data, illuminating patterns, trends, and correlations that might otherwise remain hidden. By visually exploring the data, we gain a deeper understanding of the intricate relationships between legislative language, sentiments, and policy outcomes.

### Iterative Analysis

Our methodology is not static but iterative. We continually refine our approach, incorporating feedback and insights as we progress. This iterative nature ensures that our analysis remains dynamic, responsive to emerging patterns, and adaptable to evolving legislative landscapes.

### Ethical Considerations

Throughout the entire process, we remain steadfast in our commitment to ethical research practices. We uphold the highest standards of data privacy and adhere to ethical guidelines, ensuring that our research respects the rights and confidentiality of all stakeholders involved.

In summary, our method of inquiry is a meticulously crafted, multi-stage process that combines data collection, preprocessing, advanced NLP techniques, sentiment analysis, data visualization, and ethical considerations. This comprehensive approach equips us with the tools and insights necessary to unravel the emotional dimensions of gun control legislation in the U.S. Congress, shedding light on this critical issue from a novel perspective.

## Key Sources

[1] O. Pichardo-Lagunas, B. Martinez-Seis, M. Hidalgo-Reyes, and S. Miranda, “Automatic detection of opposition relations in legal texts using sentiment analysis techniques: A case study,” _Acta Polytechnica Hungarica_, vol. 19, no. 10, pp. 165–184, 2022. doi: 10.12700/aph.19.10.2022.10.10

[2] E. Laschever and D. S. Meyer, “Growth and decline of opposing movements: Gun control and gun rights, 1945–2015\*,” _Mobilization: An International Quarterly_, vol. 26, no. 1, pp. 1–20, Mar. 2021. doi: 10.17813/1086-671x-26-1-1

[3] A. Yadav, A. Patel, and M. Shah, “A comprehensive review on resolving ambiguities in Natural Language Processing,” _AI Open_, vol. 2, pp. 85–92, 2021. doi: 10.1016/j.aiopen.2021.05.001

[4] S. Zhang, “Sentiment classification of news text data using Intelligent Model,” _Frontiers in Psychology_, vol. 12, Sep. 2021. doi: 10.3389/fpsyg.2021.758967

[5] Y.-H. Liu and Y.-L. Chen, “A two-phase sentiment analysis approach for judgement prediction,” _Journal of Information Science_, vol. 44, no. 5, pp. 594–607, Jul. 2017. doi: 10.1177/0165551517722741
