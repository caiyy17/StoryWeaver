using System;

[Serializable]
public struct PythonEnvironment
{
    public string PythonAddress;
    public string ScriptAddress;
    public string ResultAddress;
}

[Serializable]
public struct Answer
{
    public string answer;
}
