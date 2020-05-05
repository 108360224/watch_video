package com.example.myapplication;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import java.util.List;

public class M3u8 {
    private PyObject m3u8;
    M3u8(Python py){
        this.m3u8=py.getModule("get_m3u8");
    }
    String get_m3u8(String url){
        return this.m3u8.callAttr("get_m3u8",url).toJava(String.class);

    }
}
