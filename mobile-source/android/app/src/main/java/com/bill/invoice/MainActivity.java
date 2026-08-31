package com.bill.invoice;

import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.view.WindowManager;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

  private static final int FULLSCREEN_FLAGS =
        View.SYSTEM_UI_FLAG_LAYOUT_STABLE
      | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
      | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
      | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
      | View.SYSTEM_UI_FLAG_FULLSCREEN
      | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY;

  private void applyImmersive() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
      getWindow().setDecorFitsSystemWindows(false);
      WindowInsetsController ctrl = getWindow().getInsetsController();
      if (ctrl != null) {
        ctrl.hide(WindowInsets.Type.statusBars() | WindowInsets.Type.navigationBars());
        ctrl.setSystemBarsBehavior(
            WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
      }
    } else {
      getWindow().getDecorView().setSystemUiVisibility(FULLSCREEN_FLAGS);
    }
  }

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    applyImmersive();

    final View decor = getWindow().getDecorView();
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
      decor.setOnApplyWindowInsetsListener((v, insets) -> {
        applyImmersive();
        return v.onApplyWindowInsets(insets);
      });
    } else {
      decor.setOnSystemUiVisibilityChangeListener(visibility -> {
        if ((visibility & View.SYSTEM_UI_FLAG_FULLSCREEN) == 0) applyImmersive();
      });
    }
    decor.getViewTreeObserver().addOnGlobalLayoutListener(new android.view.ViewTreeObserver.OnGlobalLayoutListener() {
      private int calls = 0;
      @Override public void onGlobalLayout() {
        if (calls++ < 3) applyImmersive();
        else decor.getViewTreeObserver().removeOnGlobalLayoutListener(this);
      }
    });
  }

  private boolean leftDeliberately = false;

  @Override
  protected void onUserLeaveHint() {
    super.onUserLeaveHint();
    leftDeliberately = true;
  }

  @Override
  public void onRestart() {
    super.onRestart();
    if (leftDeliberately) {
      leftDeliberately = false;
      if (getBridge() != null && getBridge().getWebView() != null) {
        getBridge().getWebView().reload();
      }
    }
  }

  @Override
  public void onResume() {
    super.onResume();
    applyImmersive();
  }

  @Override
  public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus);
    if (hasFocus) applyImmersive();
  }
}
