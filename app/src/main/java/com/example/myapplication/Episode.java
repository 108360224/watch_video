package com.example.myapplication;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import java.util.List;

public class Episode {

    private PyObject episode;
    public Episode_list episode_list;
    Episode(Python py,String url){
        this.episode = py.getModule("episode").callAttr("Episode",url);
        this.episode_list = new Episode_list(this.episode);
    }


}
class Episode_list{
    public List<PyObject> url_list;
    public List<PyObject> text_list;
    private PyObject episode;
    Episode_list(PyObject episode){
        this.episode=episode;
        List<PyObject> gl=this.episode.callAttr("get_ep_list").asList();
        this.url_list = gl.get(1).asList();
        this.text_list=gl.get(0).asList();
    }

    String url(int i){
        return this.url_list.get(i).toJava(String.class);
    }
    String text(int i){
        return this.text_list.get(i).toJava(String.class);
    }

}