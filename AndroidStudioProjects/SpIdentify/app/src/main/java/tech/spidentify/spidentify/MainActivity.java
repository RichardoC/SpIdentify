package tech.spidentify.spidentify;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.Display;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RemoteViews;
import android.widget.TextView;
import android.widget.Toast;
import android.Manifest;

import uk.co.markormesher.android_fab.FloatingActionButton;
import uk.co.markormesher.android_fab.SpeedDialMenuAdapter;

public class MainActivity extends Activity {
    private static int RESULT_LOAD_IMG = 1;
    String imgDecodableString;

    private TextView output;
    protected ImageView logo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        logo = (ImageView) findViewById(R.id.imageView);
        output = (TextView) findViewById(R.id.textView);


        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setIcon(R.drawable.ic_add_white_24dp);
        fab.setMenuAdapter(new SpeedDial());
    }

    public void loadImagefromGallery() {
        // Create intent to Open Image applications like Gallery, Google Photos
        Intent galleryIntent = new Intent(Intent.ACTION_PICK,
                android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        // Start the Intent
        startActivityForResult(galleryIntent, RESULT_LOAD_IMG);
    }

//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        try {
//            // When an Image is picked
//            if (requestCode == RESULT_LOAD_IMG && resultCode == RESULT_OK
//                    && null != data) {
//                // Get the Image from data
//
//                Uri selectedImage = data.getData();
//                String[] filePathColumn = { MediaStore.Images.Media.DATA };
//
//                // Get the cursor
//                Cursor cursor = getContentResolver().query(selectedImage,
//                        filePathColumn, null, null, null);
//                // Move to first row
//                cursor.moveToFirst();
//
//                int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
//                imgDecodableString = cursor.getString(columnIndex);
//                cursor.close();
//                ImageView imgView = (ImageView) findViewById(R.id.imgView);
//                // Set the Image in ImageView after decoding the String
//                imgView.setImageBitmap(BitmapFactory
//                        .decodeFile(imgDecodableString));
//
//            } else {
//                Toast.makeText(this, "You haven't picked Image",
//                        Toast.LENGTH_LONG).show();
//            }
//        } catch (Exception e) {
//            Toast.makeText(this, "Something went wrong", Toast.LENGTH_LONG)
//                    .show();
//        }
//
//    }

    static final int REQUEST_IMAGE_CAPTURE = 1;

    private void takeImage() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {

            output.setText("Image loaded successfully");
        }
    }

    protected class SpeedDial extends SpeedDialMenuAdapter{

        @Override
        protected int getCount() {
            return 2;
        }

        @Override
        protected MenuItem getViews(Context context, int position) {
            MenuItem menuItem = new MenuItem();
            switch (position) {
                case 0 :
                    menuItem.labelString = "Take photo";
                    menuItem.iconDrawableId = R.drawable.ic_camera_white_24dp;
                    return menuItem;
                case 1 :
                    menuItem.labelString = "Load image";
                    menuItem.iconDrawableId = R.drawable.ic_insert_photo_white_24dp;
                    return menuItem;
            }

            return null;
        }

        @Override
        protected boolean onMenuItemClick(int position) {
            switch (position) {
                case 0 :
                    takeImage();
                    break;
                case 1 :
                    loadImagefromGallery();
                    break;
            }

            return true;
        }

        @Override
        protected boolean rotateFab() {
            return true;
        }
    }

}