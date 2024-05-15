from crewai import Agent
from crewai_tools import tool


@tool
def multiplication_tool(nums: list[str]) -> list[str]:
    """When subject data is came then return all thsoe into an arrays format"""
    return nums


class NewAgents:
    def SubjectAgent(self):
        return Agent(
            role="Subject Agent Expert",
            goal="""Identifies and outputs a list of academic subjects based on curriculum requirements or user preferences. in India for class 8. """,
            backstory=""" You are best Agent to get subject.""",
            verbose=True,
            tools=[multiplication_tool],
            allow_delegation=False,
            memory=True,
        )

    def ChapterAgent(self, subject):
        return Agent(
            role=f"""Chapter Expert""",
            goal=f"""For ${subject} subject, generates a list of chapters or major topics that comprehensively cover the subject matter.""",
            backstory="""You are best Agent to get chapters.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def TopicAgent(self):
        return Agent(
            role="Topic Agent Expert",
            goal="""Decomposes each chapter into more detailed topics that need to be covered to ensure thorough understanding.""",
            backstory=""" You are best Agent to get to cover all the topic. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def SubtopicAgent(self):
        return Agent(
            role="Subtopic Agent Expert",
            goal="""Further breaks down each topic into subtopics to facilitate detailed instruction and learning activities. """,
            backstory=""" You are best Agent to get to cover all the Subtopic. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def ContentDevelopmentAgent(self):
        return Agent(
            role="Content Development Agent Expert",
            goal=""" Expands each subtopic by generating comprehensive content, including explanations, examples, and illustrations. """,
            backstory=""" You are best Agent to get to cover all the Content Development Agent. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def AssessmentGenerationAgent(self):
        return Agent(
            role="Assessment Generation Agent Expert",
            goal=""" Creates quizzes and exercises for each chapter or topic to assess understanding and reinforce learning. """,
            backstory=""" You are best Agent to get to cover Assessment Generation. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def ReviewandAdjustmentAgent(self):
        return Agent(
            role="Review and Adjustment Agent Expert",
            goal="""Reviews the generated curriculum for completeness, coherence, and alignment with educational standards. 
            Suggests adjustments or enhancements based on feedback loops from user interactions and test results.""",
            backstory="""You are best Agent to get to cover Review and Adjustment.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
