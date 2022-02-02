
# The Programmer's Brain by Felienne Hermans

## Chapter 1
- Your LTM stores information you have acquired for a long time, the STM temporarily stores information you have just read or heard, and the working memory processes information and forms new thoughts.
- Lack of Knowledge = Issue in LTM (long time memory)
- Lack of information = Issue in STM (short time memory)
- Lack of processing power = Issue in Working memory
- To resolve confusion you must first identify its source. Confusion while coding is usually caused by three issues: a lack of knowledge, a lack of easy-to-access information, or a lack of processing power in the brain.
- Three cognitive processes are involved when you read or write code: long term memory (LTM), short term memory (STM), and working memory.
- LTM stores knowledge thatmay need to be accessed after a long period of time. For example, the meaning of keywords is stored in LTM.
- STM can temporarily hold information like the name of a method or variable.
- Working memory is where active processing takes place. In code, this may be tasks such as deciding that an index is one too low.
- All three cognitive processes are at work while you’re reading code, and the processes complement each other. For example, if your STM encounters a variable name like n, your brain searches your LTM for related programs you’ve read in the past. And when you read an ambiguous word, your working memory is activated and your brain will try to decide the right meaning in this context.

## Chapter 2
- Research has shown that when code contains comments, programmers will take more time to read its
- The STM has a capacity of two to six elements.
- To overcome the size limitation, your STM collaborates with your LTM when you remember information.
- When you read new information, your brain tries to divide the information into recognizable parts called chunks.
- When you lack enough knowledge in your LTM, you have to rely on low-level reading of code, like letters and keywords. When doing that, you will quickly run out of space in your STM.
- When your LTM stores enough relevant information, you can remember abstract concepts like “a for-loop in Java” or “selection sort in Python” instead of the code at a lower level, occupying less space in your STM.
- When you read code, it is first stored in the iconic memory. Only a bit of the code is subsequently sent to the STM.
- Remembering code can be used as a tool for (self) diagnosis of your knowledge of coding. Because you can most easily remember what you already know, the parts of code that you remember can reveal the design patterns, programming constructs, and domain concepts you are most familiar with.
- Code can contain characteristics that make it easier to process, such as design patterns, comments, and explicit beacons.

## Chapter 3
- It’s important to know quite a bit of syntax by heart because more syntax knowledge will ease chunking. Also, looking up syntax can interrupt your work
- You can use flashcards to practice and remember new syntax, with a prompt on one side and code on the other side.
- You can use flashcards to practice and remember new syntax, with a prompt on one side and code on the other side.
- It’s important to practice new information regularly to fight memory decay.
- The best kind of practice is retrieval practice, where you try to remember information before looking it up.
- To maximize the amount of knowledge you remember, spread your practice over time.
- Information in your LTM is stored as a connected network of related facts.
- Active elaboration of new information helps strengthen the network of memories the new memory will connect to, easing retrieval.

## Chapter 4
- sometimes you might want to refactor code not to make it more maintainable in the long run but more readable for you at that point in time

## Chapter 5
- Writing a summary of code in natural language will help you gain a deeper understanding of whatâ€™s happening in that code.
- A final strategy from text comprehension that we can apply to code comprehension is summarizing what you have just read
- One technique that can be helpful for very complex code of which a deeper understanding is needed is to list all operations in which variables are involved.
- Once you have created the list of identifiers, you can use it to gain a deeper understanding of the code. For example, you can divide the variable names into two different categories: names of variables that are related to the domain of the code, such as Customer or Package, and variable names that are related to programming concepts, such as Tree or Lis
- When reading code, it is important to keep track of what you are reading and whether you understand i
- Siegmundâ€™s findings reliably showed that program comprehension activates five Brodmann areas, all located in the left hemisphere of the brain: BA6, BA21, BA40, BA44, and BA4.
- An fMRI machine can detect which Brodmann areas are active by measuring blood flow in the brain
- To be able to know where to start, you need to understand how the framework links code together
- The focal point of code is an important notion when reading code. Simply put, you have to know where to start reading.
- Plan knowledge, on the other hand, represents understanding what a programmer planned when they created the program or what they were aiming to achieve.
- According to Penningtonâ€™s model, text structure knowledge relates to surface-level understanding of parts of the program, such as knowing what a keyword does or knowing the role of a variable.

## Chapter 8
- Knowledge you already have stored in your LTM can be transferred to new situations. Sometimes existing knowledge helps you learn faster or perform new tasks better. This is called positive transfer.
- Transfer of knowledge from one domain to another can also be negative, which happens when existing knowledge interferes with learning new things or executing new tasks.
- You can use positive transfer to learn new things more effectively by actively searching for related information in your LTM (for example, by elaboration, as covered earlier in the book).
- You may hold misconceptions, which occur when you are sure you are right but are actually wrong.
- Misconceptions are not always addressed by simply realizing or being told you are wrong. For misconceptions to be fixed, you need a new mental model to replace the old, wrong model.
- Even if you have learned a correct model, there is always the risk you will fall back to using the misconception.
- Use tests and documentation within a codebase to help prevent misconceptions.

## Chapter 9
- There are different perspectives on what makes a good name, ranging from syntactic rules, such as using camel case, to emphasis on consistency within a codebase.
- Without other differences, camel case variables are easier to remember than variables written in snake case, but people are quicker to identify variables when using snake case
- Locations in code where bad naming occur are also more likely to contain bugs, but that does not necessarily mean there is a causation.
- There are many different name molds used to shape variable names, but limiting yourself to a smaller number of molds will likely help comprehension.
- Applying Feitelson’s three-step model (what concepts to use in a name, what words to use for those concepts, and how to combine them) leads to higher quality names.
- Code smells, such as long methods, indicate structural issues with code. There are different cognitive reasons why code smells cause a higher cognitive load. Duplicated code, for example, makes it harder to chunk code properly, while long parameter lists are heavy on your working memory
- There are different ways to measure cognitive load, including biometric sensors like measuring blinking rate or skin temperature. If you want to measure your own cognitive load, the Paas Scale typically is a reliable instrument.
- Linguistic antipatterns indicate places in a codebase where code does something different than names involved suggest, leading to a higher cognitive load. This is likely caused by the fact that your LTM finds wrong facts while trying to support your thinking. Linguistic antipatterns can also lead to wrong chunking because your brain assumes a meaning of code that is not actually implemented

## Chapter 10
- While many people in programming argue that problem solving is a generic skill, it is not. Your prior knowledge of programming, coupled with the current problem you are solving, influence how quickly you can solve programming problems.
- Your LTM stores different types of memories, which all play a different role when solving problems. The two overarching categories of memories are implicit and explicit memories. Implicit memories are “muscle memories,” tasks you can execute without thinking about them, like touch typing. Explicit memories are memories you are aware of that you need to actively recall, such as the syntax of a for-loop.
- To strengthen your implicit memories related to programming, it is best to automatize related skills, such as touch typing and memorizing relevant keyboard shortcuts.
- To strengthen your explicit memories related to programming, study existing code, preferably with an explanation about how the code was designed.

## Chapter 11
- When you are programming, you perform a combination of different programming activities: searching, comprehending, transcription, incrementation, and exploration. Each activity puts pressure on different memory systems. Therefore, each activity should be supported by different techniques.
- Interruptions while you are programming are not only annoying; they are detrimental to productivity because it takes time to rebuild your mental model of the code.
- To better deal with interruptions, offload mental models into notes, documentation, or comments.
- Deliberately support your prospective memory if you cannot complete a task by documenting your plans.
- Try to limit interruptions to moments you experience low cognitive load, for example, through automation using a FlowLight or manually by setting your status in Slack.CDN is a framework that helps programmers predict the cognitive effect programming languages will have on their users.

## Chapter 12
- CDN is a ramework that helps programmers predict the cognitive effect programming languages will have on their users.f
- CDCB is an extension of CDN that helps programmers understand the impact their codebases, libraries, and frameworks will have on their users.
- In many cases, trade-offs between different dimensions must be made. Improving one dimension might decrease another dimension.
- Improving the design of existing codebases according to the notations framework’s cognitive dimension can be done with a design maneuver.
- Different activities place different demands on the dimensions a codebase optimizes for.

## Chapter 13
- Experts think and act differently from beginners. Experts can reason abstractly about code and have the ability to think about it without referring to the code itself. Beginners tend to focus on details in the code and have a hard time stepping back from details.
- When midlevel programmers learn new information, they sometimes fall back to beginner-level thinking.
- People who are learning a new concept need to learn about it in both abstract terms and in concrete examples.
- People who are learning a new concept also need time to connect a new concept to prior knowledge.
- When onboarding, limit the programming activities newcomers perform to one at a time.
- When onboarding, prepare relevant information to support the onboardee’s long-term, short-term, and working memory.

