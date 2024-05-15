from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
from djangobackend.Task import Tasks
from djangobackend.Agent import Agents
from crewai import Crew, Process
from langchain_openai import ChatOpenAI


@csrf_exempt
async def Excute(request):
    try:
        MathematicsExpert = Agents().MathematicsExpert()
        DetailOfChapterInMathematicsAgent = Agents().DetailOfChapterInMathematicsAgent()

        EnglishExpert = Agents().EnglishExpert()
        DetailOfChapterInEnglishAgent = Agents().DetailOfChapterInEnglishAgent()

        ScienceExpert = Agents().ScienceExpert()
        DetailOfChapterInScienceAgent = Agents().DetailOfChapterInScienceAgent()

        HistoryExpert = Agents().HistoryExpert()
        DetailOfChapterInHistoryAgent = Agents().DetailOfChapterInHistoryAgent()

        GeographyExpert = Agents().GeographyExpert()
        DetailOfChapterInGeographyAgent = Agents().DetailOfChapterInGeographyAgent()

        MathematicsTask = Tasks().MathematicsTask(MathematicsExpert)
        DetailOfChapterInMathematicsTask = Tasks().DetailOfChapterInMathematicsTask(
            DetailOfChapterInMathematicsAgent, MathematicsTask
        )
        EnglishTask = Tasks().EnglishTask(EnglishExpert)
        DetailOfChapterInEnglishTask = Tasks().DetailOfChapterInEnglishTask(
            DetailOfChapterInEnglishAgent, EnglishTask
        )
        ScienceTask = Tasks().ScienceTask(ScienceExpert)
        DetailOfChapterInScienceTask = Tasks().DetailOfChapterInScienceTask(
            DetailOfChapterInScienceAgent, ScienceTask
        )
        HistoryTask = Tasks().HistoryTask(HistoryExpert)
        DetailOfChapterInHistoryTask = Tasks().DetailOfChapterInHistoryTask(
            DetailOfChapterInHistoryAgent, HistoryTask
        )
        GeographyTask = Tasks().GeographyTask(GeographyExpert)
        DetailOfChapterInGeographyTask = Tasks().DetailOfChapterInGeographyTask(
            DetailOfChapterInGeographyAgent, GeographyTask
        )

        crew = Crew(
            agents=[
                MathematicsExpert,
                DetailOfChapterInMathematicsAgent,
                EnglishExpert,
                DetailOfChapterInEnglishAgent,
                ScienceExpert,
                DetailOfChapterInScienceAgent,
                HistoryExpert,
                DetailOfChapterInHistoryAgent,
                GeographyExpert,
                DetailOfChapterInGeographyAgent,
            ],
            tasks=[
                MathematicsTask,
                DetailOfChapterInMathematicsTask,
                EnglishTask,
                DetailOfChapterInEnglishTask,
                ScienceTask,
                DetailOfChapterInScienceTask,
                HistoryTask,
                DetailOfChapterInHistoryTask,
                GeographyTask,
                DetailOfChapterInGeographyTask,
            ],
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-4-turbo"),
            # embedder={"provider": "openai", "config": {"model": "gpt-4-1106-preview"}},
        )
        result = crew.kickoff()
        # ans=[]

        # html_content=await FrontendCode()
        # data=solve(html_content)
        # ans.append({"FrontendCode":data})

        # html_content=await BackendCode()
        # data=solve(html_content)
        # ans.append({"BackendCode":data})

        return JsonResponse("wait we are finding your answer", safe=False)
    except Exception as error:
        print("Error is ok ######### ", error)
        return JsonResponse(
            [
                {
                    "ConnectToDataBaseOutput": "Your maximum context is reached or your query is invalid. Please refresh this page and write your query again."
                }
            ],
            safe=False,
        )


current_directory = os.path.dirname(os.path.abspath(__file__))
backendcode_directory = os.path.dirname(current_directory)


async def FrontendCode():
    markdown_file_path = os.path.join(backendcode_directory, "frontendcode.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    return markdown_content


async def BackendCode():
    markdown_file_path = os.path.join(backendcode_directory, "Backendoutput.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    return markdown_content


def solve(string):

    ans = []
    # start
    ans.append({"code": string})
    return ans
    # end
    n = len(string)
    word = ""
    i = 0
    while i < n:
        if (
            i + 2 < n
            and string[i] == "`"
            and string[i + 1] == "`"
            and string[i + 2] == "`"
        ):
            ans.append({"text": word})
            word = ""
            j = i + 3
            while j < n:
                if (
                    j + 2 < n
                    and string[j] == "`"
                    and string[j + 1] == "`"
                    and string[j + 2] == "`"
                ):
                    ans.append({"code": word})
                    i = j + 2
                    word = ""
                    break
                else:
                    word += string[j]
                j += 1
        else:
            word += string[i]
        i += 1

    if len(word) != 0:
        ans.append({"text": word})

    return ans
