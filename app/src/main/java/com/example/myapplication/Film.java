package com.example.myapplication;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import java.util.List;

public class Film {

    private PyObject film;
    public Film_list film_list;
    Film(Python py,String url){
        this.film = py.getModule("film").callAttr("Film",url);
        this.film_list = new Film_list(this.film);
    }
    void load_new_film(){
        this.film.callAttr("load_new_film");
        this.film_list = new Film_list(this.film);
    }
    void goto_area(String area){
        this.film.callAttr("goto_area",area);
        this.film_list = new Film_list(this.film);
    }

}
class Film_list{
    public List<PyObject> url_list;
    public List<PyObject> img_list;
    public List<PyObject> text_list;
    private PyObject film;
    Film_list(PyObject film){
        this.film=film;
        List<PyObject> gl=this.film.callAttr("get_film_list").asList();
        this.url_list = gl.get(0).asList();
        this.img_list = gl.get(2).asList();
        this.text_list=gl.get(1).asList();
    }
    String img(int i){
        return this.img_list.get(i).toJava(String.class);
    }
    String url(int i){
        return this.url_list.get(i).toJava(String.class);
    }
    String title(int i){
        return this.text_list.get(i).toJava(String.class);
    }

}
