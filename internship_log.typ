#set page(margin: 1in)
#set par(leading: 0.55em, first-line-indent: 1.8em, justify: false)
#set text(font: "New Computer Modern")
#show raw: set text(font: "New Computer Modern Mono")
#show par: set block(spacing: 0.55em)
#show heading: set block(above: 1.4em, below: 1em)
#show link: underline

= Internship Log

== Weekly Meetings -- 22 hours
- February 8th
- February 15th
- February 29th
- March 7th
- March 14th
- March 21st
- March 28th
- April 4th
- April 11th
- April 18th
- April 25th
\
- General Notes I found useful:
  - Paper name: #link(
      "https://arxiv.org/abs/2402.03310",
    )[V-IRL: Grounding Virtual Intelligence in Real Life]
    - LLM uses knowledge about agents using bibliographies and the environment using
      APIs to develop AI agents that can sense, think, and act as humans in the real
      world
  -

== Project Meetings -- 5 hours
- February 14th
  - Went over the basis paper and reviewed the test environments
  - Discussed why the paper was rejected
  - Task: Look into environments that utilize PyTorch instead of Tensorflow
- February 28th
  - Quickly went over a list of possible reinforcement learning environments
  - Brainstormed ideas for tasks and environments
  - Received access to a previously built environment but with no RL model
  - Task: Work on a simple DQN to train a policy that can use the GridWorld
    environment to navigate to the goal
- March 6th
  - Went over code for DQN and explained the functionality
  - Task: Finish the DQN, save the trained model in a .pth file, and implement it back into the GridWorld environment to ensure the optimal path is being taken
- March 13th
  - Go over the literature review of the RL constraints field and understand how other environments use constraints
  - Task: Start implementing the second environment for testing
- March 20th
- March 27th
- April 3rd
- April 10th
- April 17th
- April 24th

