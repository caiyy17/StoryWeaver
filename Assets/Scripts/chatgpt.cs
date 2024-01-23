using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class chatgpt : MonoBehaviour
{
    
    public string path = "Assets/Scripts/env.json";
    PythonEnvironment env = new PythonEnvironment();
    string pythonPath;
    string pythonScript;
    
    void Start()
    {
        string jsonFromFile = File.ReadAllText(path);
        env = JsonUtility.FromJson<PythonEnvironment>(jsonFromFile);
        pythonPath = env.PythonAddress;
        pythonScript = env.ScriptAddress;

        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = pythonPath; // 或者 python 的完整路径
        start.Arguments = pythonScript; // Python脚本的路径
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;

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
