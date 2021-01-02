package hello;

import java.lang.Thread;
import java.util.Random;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {

  @RequestMapping("/hello")
  public String hello() {
    Random random = new Random();
    try {
        Thread.sleep(50 + random.nextInt(26));
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    return "Hello world!";
  }

  @RequestMapping("/health")
  public String health() {
    Random random = new Random();
    try {
        Thread.sleep(75);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    return "Ok";
  }

  @RequestMapping("/")
  public String root() {
    return "Ok";
  }
}
