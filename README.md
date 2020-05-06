# watch_video



Menu 
-

- **Menu**(***Python*** `py`)
	- **Menu\_list** menu_list
- **Menu_list**
	- url_list
	- text_list
	- ***String*** text(***int*** `id`) 
		- return index(`id`) of text_list
	- ***String*** url(***int*** `id`)
		- return index(`id`) of url_list
	- **Child_list** child\_list(***int*** `id`)
		- return index(`id`) of child_list
- **Child_list**
	- url_list
	- text_list
	- ***String*** text(***int*** `id`) 
		- return index(`id`) of text_list
	- ***String*** url(***int*** `id`)
		- return index(`id`) of url_list


Film 
-
- **Film**(***Python*** `py`,***String*** `url`)
	- **Film\_list** film_list
- ***void*** load\_new\_film()
	- update film_list to next page
- ***void*** goto_area(***String*** `area`)
	- update film_list to `area`
		- `area`:"香港","台灣","大陸","日本","韓國","歐美","泰國","新馬","印度","海外"
- ***void*** sort_by(***String*** `order`)
	- update film_list to `order`
		- `order`:"vod\_addtime","vod\_hits","vod\_hits\_month","vod\_hits\_day","vod\_hits\_week","vod\_gold","vod\_golder","vod\_up"
- **Film_list**
 	- url_list
	- text_list
	- img_list
		- img\_src\_list
	- ***String*** url(**int** `id`)
		- return index(`id`) of url_list
	- ***String*** text(**int** `id`) 
		- return index(`id`) of title_list
	- ***String*** img(**int** `id`) 
		- return index(`id`) of img_list

Episode 
-
- **Episode**(***Python*** `py`,***String*** `url`)
	- **Episode\_list** episode _list
- **Episode\_list**
	- url_list
	- text_list
	- ***String*** text(***int*** `id`) 
		- return index(`id`) of text_list
	- ***String*** url(***int*** `id`)
		- return index(`id`) of url_list

M3u8
-
- **M3u8**(***Python*** `py`)
- ***String*** get\_m3u8(***String*** `url`)
	- return https://......index.m3u8
	- if not exit return "not exit"

Search 
-
- **Search**(***Python*** `py`)
	- **Search\_list** search _list
- ***void*** search(***String*** `keyword`)
	- update search _list to new keyword
- **Search\_list**
	- url_list
	- text_list
	- img_list
		- img\_src\_list
	- ***String*** url(**int** `id`)
		- return index(`id`) of url_list
	- ***String*** title(**int** `id`) 
		- return index(`id`) of text_list
	- ***String*** img(**int** `id`) 
		- return index(`id`) of img_list


----------

example
-
```java
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
```

    
