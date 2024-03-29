using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class chatgpt : MonoBehaviour
{
    public string question = "Hello";
    public string path = "Assets/Scripts/env.json";
    PythonEnvironment env = new PythonEnvironment();
    string pythonPath;
    string pythonScript;
    string resultPath;
    Answer ans = new Answer();
    ProcessStartInfo start = new ProcessStartInfo();

    void Start()
    {
        string jsonFromFile = File.ReadAllText(path);
        env = JsonUtility.FromJson<PythonEnvironment>(jsonFromFile);
        pythonPath = env.PythonAddress;
        pythonScript = env.ScriptAddress;
        resultPath = env.ResultAddress;

        start.FileName = pythonPath;
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;
        string temp = AskGPT(question, 999);
        Parse();
        // TTS(temp);
        // GenerateImage(temp);
    }

    string AskGPT(string prompt, int id = 0)
    {
        start.Arguments = pythonScript + " ask \"" + prompt + "\" " + id.ToString();
        using(Process process = Process.Start(start))
        {
            using(StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log(result);
            }
        }
        string jsonFromFile = File.ReadAllText(resultPath + ".json");
        ans = JsonUtility.FromJson<Answer>(jsonFromFile);
        UnityEngine.Debug.Log("answer: " + ans.answer);
        return ans.answer;
    }

    void TTS(string prompt)
    {
        start.Arguments = pythonScript + " tts \"" + prompt + "\"";
        using(Process process = Process.Start(start))
        {
            using(StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log(result);
            }
        }
    }

    void GenerateImage(string prompt)
    {
        start.Arguments = pythonScript + " image \"" + prompt + "\"";
        using(Process process = Process.Start(start))
        {
            using(StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log(result);
            }
        }
    }

    void Parse()
    {
        start.Arguments = pythonScript + " parse";
        using(Process process = Process.Start(start))
        {
            using(StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log(result);
            }
        }
        // string jsonFromFile = File.ReadAllText(resultPath + "_parsed.json");
        // ans = JsonUtility.FromJson<Answer>(jsonFromFile);
    }
}
