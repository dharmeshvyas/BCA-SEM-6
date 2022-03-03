package com.example.timepicker;

import androidx.appcompat.app.AppCompatActivity;

import android.app.TimePickerDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TimePicker;
import android.widget.Toast;
import java.sql.Time;
import java.text.SimpleDateFormat;

public class MainActivity extends AppCompatActivity {

    TimePicker timePicker;
    TimePickerDialog tp;
    EditText edt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        edt = findViewById(R.id.ed);
        edt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    tp = new TimePickerDialog(MainActivity.this, new TimePickerDialog.OnTimeSetListener() {
                        @Override
                        public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                            Time time = new Time(hourOfDay, minute, 0);
                            SimpleDateFormat sdf = new SimpleDateFormat("h:mm");
                            edt.setText(sdf.format(time));
                        }
                    },0,0,false);
                }catch (Exception e){
                    Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
                }

            }
        });
    }
}