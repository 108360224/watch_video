package com.example.myapplication;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import java.util.List;

public class Menu {

    private PyObject menu;
    public Menu_list menu_list;
    Menu(Python py){
        this.menu = py.getModule("menu").callAttr("Menu");
        this.menu_list = new Menu_list(this.menu);
    }
}
class Menu_list{
    public List<PyObject> url_list;
    public List<PyObject> text_list;
    private PyObject menu;
    Menu_list(PyObject menu){
        this.menu=menu;
        List<PyObject> gl=this.menu.callAttr("get_menu_list").asList();
        this.text_list = gl.get(0).asList();
        this.url_list = gl.get(1).asList();

    }
    String text(int i){
        return this.text_list.get(i).toJava(String.class);
    }
    String url(int i){
        return this.url_list.get(i).toJava(String.class);
    }
    Child_list child_list(int i){
        return new Child_list(i,this.menu);
    }
}
class Child_list{
    public List<PyObject> url_list;
    public List<PyObject> text_list;
    Child_list(int i,PyObject menu){

        List<PyObject> gl=menu.callAttr("get_child_list").asList();
        this.text_list = gl.get(0).asList().get(i).asList();
        this.url_list = gl.get(1).asList().get(i).asList();
    }
    String text(int i){
        return this.text_list.get(i).toJava(String.class);
    }
    String url(int i){
        return this.url_list.get(i).toJava(String.class);
    }
}