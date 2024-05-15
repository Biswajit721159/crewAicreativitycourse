from crewai import Task


class NewTasks:
    def SubjectTask(self, agent):
        return Task(
            description=f""" Identifies and outputs a list of academic subjects based on curriculum requirements or user preferences.""",
            expected_output=f"""return an arrays of Subjects such as English, Science, Mathematics, History, etc.""",
            agent=agent,
            output_file="output/Subject.md",
        )

    def ChapterTask(self, agent, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=f"""For ${subject} subject, generates a list of chapters or major topics that comprehensively cover the subject matter.""",
            expected_output=f"""For ${subject} subject, chapters might be get all the chapter""",
            agent=agent,
            output_file=f"""output/${output_string}Chapter.md""",
        )

    def TopicTask(self, agent, ChapterTask, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=""" Decomposes each chapter into more detailed topics that need to be covered to ensure thorough understanding.""",
            expected_output=f"""For a chapter on Algebra, topics might include Linear Equations, Quadratic Equations, Polynomials, etc. """,
            agent=agent,
            context=[ChapterTask],
            output_file=f"""output/${output_string}Topic.md""",
        )

    def SubtopicTask(self, agent, TopicTask, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=f"""Further breaks down each topic into subtopics to facilitate detailed instruction and learning activities.""",
            expected_output=f"""For the topic give good quality description.""",
            agent=agent,
            context=[TopicTask],
            output_file=f"""output/${output_string}Subtopic.md""",
        )

    def ContentDevelopmentTask(self, agent, SubtopicTask, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=f"""Expands each subtopic by generating comprehensive content, including explanations, examples, and illustrations.""",
            expected_output=f"""Detailed educational content suitable for learning materials or direct instruction.""",
            agent=agent,
            context=[SubtopicTask],
            output_file=f"""output/${output_string}ContentDevelopment.md""",
        )

    def AssessmentGenerationTask(self, agent, ContentDevelopmentTask, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=f""" Creates quizzes and exercises for each chapter or topic to assess understanding and reinforce learning. """,
            expected_output=f"""Multiple-choice questions, short answer questions, problems to solve, case studies, etc., tailored to the specific topics and subtopics.""",
            agent=agent,
            context=[ContentDevelopmentTask],
            output_file=f"""output/${output_string}AssessmentGeneration.md""",
        )

    def ReviewandAdjustmentTask(self, agent, AssessmentGenerationTask, subject):
        output_string = subject.replace(" ", "")
        return Task(
            description=f"""Reviews the generated curriculum for completeness, coherence, and alignment with educational standards.
            Suggests adjustments or enhancements based on feedback loops from user interactions and test results.""",
            expected_output=f""" Recommendations for content improvement, updates to questions, and personalized learning paths. """,
            agent=agent,
            context=[AssessmentGenerationTask],
            output_file=f"""output/${output_string}ReviewandAdjustment.md""",
        )
