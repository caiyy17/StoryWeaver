using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class chatgpt : MonoBehaviour
{
    public string question = "Please reply that is a test";
    public string path = "Assets/Scripts/env.json";
    PythonEnvironment env = new PythonEnvironment();
    string pythonPath;
    string pythonScript;
    ProcessStartInfo start = new ProcessStartInfo();

    void Start()
    {
        string jsonFromFile = File.ReadAllText(path);
        env = JsonUtility.FromJson<PythonEnvironment>(jsonFromFile);
        pythonPath = env.PythonAddress;
        pythonScript = env.ScriptAddress;

        start.FileName = pythonPath;
        start.Arguments = pythonScript + " \"" + question + "\"";
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;
        AskGPT(question);
    }

    void AskGPT(string prompt)
    {
        start.Arguments = pythonScript + " \"" + prompt + "\"";
        using(Process process = Process.Start(start))
        {
            using(StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log(result);
            }
        }
    }
}
