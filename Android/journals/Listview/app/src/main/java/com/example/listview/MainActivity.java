package com.example.listview;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    ListView listView;
    EditText value;
    Button add;
    ArrayList<String> arrayList;
    ArrayAdapter<String> arrayAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listView = findViewById(R.id.listvw);
        value = findViewById(R.id.value);
        add = findViewById(R.id.addbtn);
        arrayList = new ArrayList<>();


            add.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Toast.makeText(MainActivity.this, "Clicked", Toast.LENGTH_SHORT).show();
                    String values =value.getText().toString();
                    if(!values.isEmpty()) {
                        arrayList.add(value.getText().toString());
                        arrayAdapter = new ArrayAdapter<>(
                                getApplicationContext(),
                                R.layout.custom_layout,
                                R.id.r_text, arrayList);
                        listView.setAdapter(arrayAdapter);
                        value.setText("", null);
                        Toast.makeText(MainActivity.this, "List added", Toast.LENGTH_SHORT).show();
                    }
                    else{
                        Toast.makeText(MainActivity.this, "Please add some value", Toast.LENGTH_SHORT).show();
                    }
                }
            });

        listView.setOnItemClickListener(
                new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> adapter, View parent, int position, long id) {
                        try{

                            String value = adapter.getItemAtPosition(position).toString();
                            Toast.makeText(MainActivity.this,value,Toast.LENGTH_LONG).show();
                        }catch (Exception e){
                            Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_LONG).show();

                        }
                    }
                }
        );
    }
}