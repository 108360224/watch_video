package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import com.chaquo.python.Kwarg;
import com.chaquo.python.PyObject;
import com.chaquo.python.android.AndroidPlatform;
import com.chaquo.python.Python;

import java.util.List;


public class MainActivity extends AppCompatActivity {
    static final String TAG = "PythonOnAndroid";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initPython();
        callPythonCode();
    }

    void initPython(){
        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
    }

    void callPythonCode(){
        Python py = Python.getInstance();


        Menu menu=new Menu(py);

        String url=menu.menu_list.child_list(2).url(1);
        Log.d(TAG,"url = "+url);
        Film film=new Film(py,url);
        String f1=film.film_list.url(0);
        film.load_new_film();
        film.goto_area("日本");
        String f2=film.film_list.url(1);
        String img=film.film_list.img(0);
        Log.d(TAG,"f1 = "+f1+"f2="+f2+"img="+img);
        Episode episode=new Episode(py,f2);
        String eps=episode.episode_list.url(0);
        Log.d(TAG,"eps="+eps);
        M3u8 get_m3u8=new M3u8(py);
        String m3u8=get_m3u8.get_m3u8(eps);
        Log.d(TAG,"m3u8="+m3u8);
        Search search=new Search(py);
        search.search("好 好");
        String s=search.search_list.url(0);
        Log.d(TAG,"search="+s);
    }
}
