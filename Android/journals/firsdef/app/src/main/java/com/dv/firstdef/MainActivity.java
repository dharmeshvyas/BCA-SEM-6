package com.dv.firstdef;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText edituser;
    EditText editpass;
    Button loginbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getSupportActionBar().hide();
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        edituser =findViewById(R.id.edituser);
        editpass =findViewById(R.id.editpass);
        loginbtn =findViewById(R.id.loginbtn);

        loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String valuser =edituser.getText().toString();
                String valpass = editpass.getText().toString();

                if(valuser.equals("") && valpass.equals("")){
                    Toast.makeText(MainActivity.this,"Textbox is empty please enter information",Toast.LENGTH_LONG).show();
                }
                else{
                    try {
                        Intent intent =new Intent(getApplicationContext(),second.class);
                        intent.putExtra("valuser",valuser);
                        intent.putExtra("valpass",valpass);
                        startActivity(intent);
                    }catch (Exception e){
                        Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_LONG).show();
                    }

                }
            }
        });
    }
}