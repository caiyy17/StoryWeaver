using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class chatgpt : MonoBehaviour
{
    public string pythonPath = "";
    public string pythonScript = "";
    void Start()
    {
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
