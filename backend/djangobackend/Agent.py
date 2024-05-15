from crewai import Agent


class Agents:
    def MathematicsExpert(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest English medium syllabus for the subject of Mathematics in India for class 8. """,
            backstory=""" You are best Mathematician in india """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def DetailOfChapterInMathematicsAgent(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest descriptions for each topic in the Mathematics syllabus """,
            backstory=""" You are best Mathematician in india """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def EnglishExpert(self):
        return Agent(
            role="English Expert",
            goal=""" Please provide the latest English medium syllabus for the subject of English in India for class 8. """,
            backstory=""" You are best English expert in india.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def DetailOfChapterInEnglishAgent(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest descriptions for each topic in the Mathematics syllabus """,
            backstory=""" You are best English expert in india """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def ScienceExpert(self):
        return Agent(
            role="Science Expert",
            goal=""" Please provide the latest English medium syllabus for the subject of Science in India for class 8. """,
            backstory="""  You are best Science expert in india. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def DetailOfChapterInScienceAgent(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest descriptions for each topic in the Science syllabus """,
            backstory=""" You are best Science expert in india. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def HistoryExpert(self):
        return Agent(
            role="History Expert",
            goal="""Please provide the latest English medium syllabus for the subject of History in India for class 8.""",
            backstory="""  You are best History expert in india. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def DetailOfChapterInHistoryAgent(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest descriptions for each topic in the History syllabus """,
            backstory=""" You are best History expert in india. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def GeographyExpert(self):
        return Agent(
            role="Geography Expert",
            goal=""" Please provide the latest English medium syllabus for the subject of Geography in India for class 8. """,
            backstory=""" You are best Geography expert in india.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
    def DetailOfChapterInGeographyAgent(self):
        return Agent(
            role="Mathematics Expert",
            goal=""" Please provide the latest descriptions for each topic in the Geography syllabus """,
            backstory=""" You are best Geography expert in india. """,
            verbose=True,
            allow_delegation=True,
            memory=True,
        )