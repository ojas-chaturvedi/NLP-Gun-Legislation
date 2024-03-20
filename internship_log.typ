#set page(margin: 1in)
#set par(leading: 0.55em, first-line-indent: 1.8em, justify: false)
#set text(font: "New Computer Modern")
#show raw: set text(font: "New Computer Modern Mono")
#show par: set block(spacing: 0.55em)
#show heading: set block(above: 1.4em, below: 1em)
#show link: underline
#show link: set text(blue)

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
  - Task: Finish the DQN, save the trained model in a .pth file, and implement it
    back into the GridWorld environment to ensure the optimal path is being taken
- March 13th
  - Go over the literature review of the RL constraints field and understand how
    other environments use constraints
  - Task: Start implementing the second environment for testing
- March 20th
- March 27th
- April 3rd
- April 10th
- April 17th
- April 24th

#pagebreak()

== Personal Work
- Reviewed paper -- 14 hours
  - Paper name: #link(
      "https://proceedings.neurips.cc/paper/2021/file/72f67e70f6b7cdc4cc893edaddf0c4c6-Paper.pdf
                              ",
    )[Safe Reinforcement Learning with Natural Language Constraints]
  - Went through original paper working to solve the issue of adding natural
    language constraints to RL models
  - Notes:
    - Analogy of constraints: A cleaning robot must be careful to not knock the
      television over, even if the television lies on the optimal path to cleaning the
      house
    - Two key limitations of Safe RL algorithms:
      - Provide constraints in mathematical or logical forms, which calls for specific
        domain expertise
      - Policies trained with a specific set of constraints cannot be transferred easily
        to learn new tasks with the same set of constraints
    - Figure 1
      - Safety training -- agent learns to interpret textual constraints while learning
        the task
      - Safety evaluation -- agent learns to interpret textual constraints while
        learning the task
    - Types of constraints:
      - Budgetary constraints -- limit the frequency of being in unsafe states
      - Relational constraints -- specify unsafe states in relation to surrounding
        entities
      - Sequential constraints -- activate certain states to be unsafe based on past
        events
    - Why not instructions?
      - Instead of instructions, which specify what to do, textual constraints only
        inform the agents on what _not to do_, independent of maximizing rewards
        - To obtain rewards, the agent has to explore and figure out optimal policies on
          its own
      - Constraints are decoupled from rewards and policies, so agents trained to
        understand certain constraints can transfer their understanding to respect these
        constraints in new tasks, even when the new optimal policy is drastically
        different
    - Methodology -- POLCO (Policy Optimization with Language Constraints)
      - Constraint interpreter to encode language constraints into the representation of
        forbidden states
      - Policy network operates on these representations and state observations to
        produce actions
      - Factorizing the model in this manner allows the agent to retain its constraint
        comprehension capabilities while modifying its policy network to learn new tasks
