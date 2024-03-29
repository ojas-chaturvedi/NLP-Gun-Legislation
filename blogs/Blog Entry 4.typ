#import "@local/typst-templates:0.1.0": general_template
#show: general_template.with(
  title: "Data Collection Progress: Legislative Text Acquisition And Preliminary Classification Efforts",
  prefix: [_AP Research & Senior Research Project_],
  authors: none,
  suffix: [#link("https://github.com/ojas-chaturvedi")],
  enable-footer: true,
)

This week marked a significant milestone in my project, as I completed the initial phase of data collection by acquiring the text from congressional legislation. Resolving the VPN issue enabled access to ASU's supercomputer Sol, where I executed my script to retrieve all necessary data in JSON format. This data is now prepared for analysis through my sentiment analysis models. However, there's an additional step in data collection remaining: assigning each piece of legislation a designation as either pro-gun rights or pro-gun control. This classification will enrich the sentiment analysis models with more nuanced insights. I've recently gained access to the OpenAI Researcher Access Program through my internship lab and have begun familiarizing myself with the API documentation for data classification. Once classification is complete, I'll advance to developing my sentiment analysis models. I anticipate the model development process will span 2-3 weeks, focusing on maximizing accuracy. While working on these steps, I have also finished reading a plethora of texts that explain the concept of literature reviews and how to write them as efficiently as possible. While I have already written my literature review as a task for my AP Research class, I plan to use the valuable insights I gained to rewrite my literature review and expand on it to fully show the gap in the field that I am addressing.

During my time at the ASU Data Mining and Reinforcement Learning Lab, I have successfully developed and trained a Deep Q-network (DQN) to refine the policy guiding our reinforcement learning (RL) agent within a designated environment. From my previous update, the DQN merges the sophistication of deep learning with the fundamentals of Q-learning, a cornerstone reinforcement learning algorithm renowned for its adeptness in navigating complex, high-dimensional state spaces encountered in a plethora of real-world settings. The training phase was directed towards optimizing the reward mechanism within the illustrated environment:

#figure(
  image("./assets/3_environment.png"),
  caption: [
    Simple environment to test basic RL agent
  ],
)

This period culminated in the completion of the DQN's construction, accompanied by the analysis of reward dynamics over 10,000 iterations, graphically represented below:
#figure(
  image("./assets/4_reward.png", width: 90%),
  caption: [
    Graph of DQN reward over the number of runs
  ],
)

Post-training, I have written a script to execute a rigorous assessment of the DQN to understand its consistency in selecting the most efficient path. After conducting another 10,000 tests, consistently receiving a reward of 184 in all attempts confirmed the algorithm's accuracy. This consistency supports our initial theory that the optimal path from start to finish involves 16 steps. For a visual demonstration of the agent's flawless execution of the optimal route, refer to the following YouTube link: #link("https://youtu.be/sBKuauJbiHM"). With the foundational environment now established and effectively navigating the pre-defined constraints, the next phase of my project is to integrate natural language constraints within the environment. This task is the most complex and will enhance the RL agent's decision-making capabilities, marking a significant leap toward our objective of adding natural language constraints to reinforcement learning environments.

Next week, I plan to wrap up a classification script for the legislative texts. Making the script shouldn't be too tough, but the real challenge will be figuring out how to write ChatGPT prompts that give me consistent results. From what I've seen, asking ChatGPT the same thing twice can get you two different answers, so I need a script that gets me the same answer every time in one word. Once the sorting script is done, I'll move on to the bulk of my project: building the sentiment analysis models. This part will definitely take up most of my time. By the end of next week, I aim to have at least one model up and running, though it might not be completely adjusted yet. Meanwhile, I'll keep pushing forward with my internship and AP Research tasks.