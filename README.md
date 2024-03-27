# Legislative Narratives on Gun Control in the United States: A Multi-Model Sentiment Analysis Approach (2001-2023)

This project employs advanced multi-model sentiment analysis techniques to systematically dissect and understand the framing of gun control issues within U.S. Congressional legislation from 2001 to 2023. It aims to uncover the emotional and rhetorical strategies deployed in legislative discourse, offering insights into how these narratives influence public perception and policy-making in the realm of gun control.

### Project Setup

1. Optional: Create a Python virtual environment
2. Install all the Python requirements: `pip install -r requirements.txt`
3. **CONTINUE HERE**

**BASIS Advisor**: Travis May
**Internship Location**: Arizona State University
**Onsite Mentor**: Hua Wei, Ph.D.

### Project Description

Have you ever wondered about the power of words in shaping public opinion on contentious issues like gun control? Perhaps you hadn't considered their impact at all. My project delves into the emotional and rhetorical dynamics of U.S. Congressional bills on gun issues, spanning from the 107th to the 117th sessions (2001-2023). We aim to strip back the layers of legislative language, uncovering how the debate on gun control and rights is framed and its potential sway over societal attitudes. At the ASU Data Mining and Reinforcement Learning Lab under the expert guidance of Professor Hua Wei, I work on projects that focus on sim-to-real transfer and human-AI collaboration, specifically in optimizing traffic signal control through advanced reinforcement learning techniques. This experience sharpens my ability to navigate complex data and apply machine learning models, skills I use to dissect and analyze the sentiment of legislative texts in my own project on Congressional gun legislation. As we dissect the emotional tones and persuasive strategies within these texts, we're doing more than scrutinizing laws; we're revealing the narratives that fuel national discourse and mold public perception. The ultimate goal? To offer a lens through which we can better understand the polarized landscape of gun legislation, providing insights that could reshape how policies are communicated and perceived. Join us in this exploration of linguistic power, where every word in a bill carries the weight of conviction and the potential to shift the tides of public opinion!

### Weekly Blog Updates

For weekly updates through blog entries, check out my website: [https://basisseniorprojects.com/chandler/author/ojas_c/](https://basisseniorprojects.com/chandler/author/ojas_c/)

### Research Question

What insights can a multi-model sentiment analysis reveal about the framing of legislation containing the word 'gun' introduced in the U.S. Congress between the 107th and 117th sessions (2001-2023)?

### Background / Context

The gun control debate in the United States holds deep historical roots, tracing back to the Second Amendment. This longstanding debate has gained increased momentum in recent years, impacted by events such as the tragic Sandy Hook and Parkland shootings. These incidents have triggered legislative responses at both federal and state levels. Within this environment, proponents of gun rights and gun control advocacy groups are getting more increased divergent viewpoints, highlighting the nation's polarization on the matter.

Public opinion regarding gun-related issues has been subject to significant fluctuations, and its influence on political discourse and legislative priorities cannot be underestimated. The variability and intensity of public sentiment, often gauged through surveys and reflected in media coverage, contribute to the complexity of societal attitudes, political ideologies, and policy-making.

The U.S. Congress has grappled with this debate by introducing a wide spectrum of bills related to gun regulation and rights. This legislative diversity manifests in proposed measures ranging from the Assault Weapons Ban to laws expanding concealed carry rights, mirroring the evolving stance on gun-related matters across the nation.

#### Rationale for Using Sentiment Analysis

In addressing the complexities of the gun control debate, this study adopts a new approach by integrating sentiment analysis into the analysis of legislative language. While traditional legislative analysis predominantly scrutinizes legal and policy aspects, it often neglects the emotional and psychological dimensions that are interwoven within legislative texts. This study aligns with recent advances in Natural Language Processing (NLP), including text mining and machine learning algorithms, which have introduced innovative methods to dissect the nuanced layers of legislative bills.

Furthermore, the application of sentiment analysis to the domain of gun control legislation remains relatively unexplored, representing a significant research gap. By leveraging insights from related research fields and building upon advances in sentiment analysis, this project aspires to show the linguistic patterns and emotional undertones concealed within gun control bills. This endeavor seeks to provide a nuanced understanding of how emotions and rhetorical strategies shape legislative language and the potential ramifications of these linguistic elements on societal and political sentiments.

In essence, this study endeavors to bridge the divide between traditional legislative analysis and the evolving landscape of sentiment analysis. By doing so, it contributes to a more holistic understanding of legislative rhetoric and its emotional underpinnings, offering insights that can inform future legislative drafting, policy decisions, and political strategies in the contentious arena of gun control.

### Important Definitions

**Gun Control**: Refers to any regulation related to the manufacture, sale, transfer, possession, modification, or use of firearms.

**Second Amendment**: A part of the U.S. Constitution that safeguards the right to keep and bear arms, frequently at the core of the gun control debate.

**Legislative Bill**: A formal proposal for new legislation, presented for consideration and debate within a legislative body.

**Rhetorical Strategies**: Techniques used in arguments to influence audiences, often through appeals to emotion, logic, or credibility.

**Sentiment Analysis**: A computational process that identifies and categorizes opinions in text, aiming to ascertain the writer's attitude towards a specific topic.

**Natural Language Processing (NLP)**: An area of artificial intelligence that enables computers to understand, interpret, and manipulate human language, bridging human communication and computer understanding.

### Assumptions

**Consistency in Legislative Language**: The analysis assumes that the language used in legislative bills is consistent and structured enough to allow for accurate sentiment analysis. This includes the assumption that the language is sufficiently clear and unambiguous to be interpreted by sentiment analysis algorithms.

**Reliability and Neutrality of Analysis Tools and Process**: The project assumes the sentiment analysis tools and NLP techniques are both effective in interpreting legislative language nuances and inherently neutral, ensuring an unbiased, accurate capture of emotional tones and rhetorical strategies.

**Interplay of Societal Attitudes and External Events**: This project posits a complex relationship between stable societal attitudes and the influence of external events on legislative language, with sentiment analysis expected to detect these nuanced influences over the analyzed periods.

**Representativeness and Generalizability of Legislative Analysis**: It is assumed that the selected bills for analysis accurately reflect broader legislative trends in gun control from the 107th to 117th Congress sessions, allowing for generalization of the findings to broader federal legislative trends.

### Significance / Importance of Study

This study holds significant technical and practical importance in the field of legislative analysis, particularly in the context of gun control legislation. The utilization of sentiment analysis introduces a groundbreaking approach that addresses specific technical gaps:

- **Emotionally Informed Legislative Analysis**: Traditional legislative analysis has primarily focused on the legal and policy aspects of bills, often overlooking the emotional language and tone that shape legislative language. By incorporating sentiment analysis, this study explores the emotional and rhetorical dimensions of gun control bills, thus providing a more comprehensive understanding of legislative rhetoric. This approach is aligned with recent efforts in NLP, such as the Gun Violence Database, which emphasizes the need for sentiment-aware analysis in this domain.
- **Nuanced Emotional Tones**: Sentiment analysis not only uncovers emotional tones within legislative language but also identifies persuasive techniques and framing strategies employed by legislators. This analysis offers a nuanced perspective on how emotions are strategically woven into the language of these critical documents, offering valuable insights into lawmakers' messaging on the contentious issue of gun control. It aligns with studies like Pichardo-Lagunas et al.'s work on detecting opposition relations in legal texts using sentiment analysis techniques.
- **Advancing Sentiment Analysis in Legislation**: This study represents a new and creative application of sentiment analysis techniques to legislative analysis. Leveraging advanced NLP methods, it pushes the boundaries of sentiment analysis, showcasing its adaptability in deciphering the intricate nuances of legal texts. This methodological advancement sets a precedent for future research, not only in the realm of gun control but across various legislative domains, opening doors to a deeper comprehension of legislative language and sentiment. This approach is consistent with the broader trend in NLP research, as evidenced by studies like Yadav et al.'s comprehensive review on resolving ambiguities in Natural Language Processing and Liu and Chen's two-phase sentiment analysis approach for judgment prediction.

Additionally, this study aligns with the work of Laschever and Meyer, who have examined the growth and decline of opposing movements in gun control and gun rights. By delving into the emotional and rhetorical dimensions of gun control legislation, this research contributes to the growing body of knowledge on this important issue, shedding light on the intricate dynamics of legislative language and sentiment in the context of gun control, and the effect they have on public perception.

### Method of Inquiry

1. **Data Collection**: Utilizing a self-made web scraper and Congress.gov API, we systematically gather data on congressional gun legislation introduced in the U.S. Congress during the 107th to 117th sessions. This data is structured in JSON format to provide a comprehensive overview of legislative activities.
2. **Data Preprocessing**: After data collection, a crucial preprocessing step is undertaken. This involves data cleansing to remove any extraneous information such as duplicates, incomplete records, and irrelevant metadata. Additionally, we anonymize any personally identifiable information to ensure data privacy and ethical research practices.
3. **Large Language Models (LLM)**: We employ large language models to categorize each gun legislation. These models use advanced Natural Language Processing techniques to analyze the textual content and categorize the bills effectively.
4. **Sentiment Analysis Model Training**: To enhance the accuracy of previously made sentiment analysis models, such as VADER or Legal-BERT, we fine-tune existing sentiment analysis models using new data specifically related to legal gun terms. This step ensures that our sentiment analysis models are well-versed in the nuances of legislative language.
5. **Model Evaluation and Scoring**: We run all the sentiment analysis models on the entire dataset, generating sentiment scores for each piece of legislation. These scores are then averaged across the different sentiment analysis models to ensure robustness and reliability.
6. **Data Visualization**: Using data visualization tools, such as the MatPlotLib python library, to create compelling visual representations of the sentiment analysis results. These visualizations provide a clear overview of emotional tones and rhetorical strategies within the legislation.
7. **Statistical Correlation Analysis**: We employ statistical correlation analysis to quantitatively measure the relationships between emotional tones within the legislation and subsequent policy outcomes. This method provides empirical insights into how sentiment in legislative language may influence legislative intent and policy decisions.
   1. **Variable Selection**: Identify the relevant variables for correlation analysis, which include sentiment scores (positive, negative, neutral), legislative intent, and policy outcomes.
   2. **Correlation Coefficient Calculation**: Calculate the correlation coefficients between pairs of selected variables, quantifying the strength and direction of their relationships.
   3. **Interpretation**: Interpret the correlation coefficients to understand how emotional tones in legislative language correlate with legislative intent and policy outcomes.
   4. **Significance Testing**: Perform significance testing to determine the statistical significance of observed correlations, ensuring that the relationships are not due to chance.
   5. **Visualization**: Create visual representations, such as scatterplots or correlation matrices, to visually depict the relationships between variables.
