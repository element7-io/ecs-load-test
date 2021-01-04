package hello;

import java.lang.Thread;
import java.util.Random;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {

  @RequestMapping("/hello")
  public String hello() {
    try {
        Thread.sleep(250);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    return "Hello world!";
  }

  @RequestMapping("/slow")
  public String slow() {
    Random random = new Random();
    try {
        Thread.sleep(1000 * random.nextInt(11));
    } catch (InterruptedException e) {
        System.out.println(e.getMessage());
    }
    return "Auch";
  }

  @RequestMapping("/health")
  public String health() {
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
