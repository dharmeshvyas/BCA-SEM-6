package com.dv.firstdef;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;

public class second extends AppCompatActivity {

    EditText usertxt;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        usertxt = findViewById(R.id.secondtext);
        usertxt.setText("Welcome "+ getIntent().getStringExtra("valuser"));
    }
}