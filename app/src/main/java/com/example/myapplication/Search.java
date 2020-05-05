package com.example.myapplication;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import java.util.List;

public class Search {
    private PyObject search;
    public Search_list search_list;
    Search(Python py){
        this.search=py.getModule("search");
    }
    void search(String word){
        this.search_list=new Search_list(this.search,word);
    }
}
class Search_list{
    public List<PyObject> url_list;
    public List<PyObject> text_list;
    public List<PyObject> img_list;
    private PyObject search;
    Search_list(PyObject search,String word){
        this.search=search;
        List<PyObject> sl=this.search.callAttr("search",word).asList();
        this.url_list = sl.get(0).asList();
        this.text_list = sl.get(1).asList();
        this.img_list = sl.get(2).asList();
    }
    String url(int i){
        return this.url_list.get(i).toJava(String.class);
    }
    String text(int i){
        return this.text_list.get(i).toJava(String.class);
    }
    String img(int i){
        return this.img_list.get(i).toJava(String.class);
    }
}
