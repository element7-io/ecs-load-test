package hello;

import java.lang.Thread;
import java.util.Random;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.http.ResponseEntity;
import org.springframework.beans.factory.annotation.Autowired;
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Gauge;
import org.springframework.http.HttpStatus;


@RestController
public class HelloController {

  @Autowired
  private MeterRegistry repo;

  @RequestMapping("/hello")
  @ResponseBody
  public ResponseEntity hello() {
    try {

        Gauge busyThreads = repo.get("tomcat.threads.busy").gauge();
        Gauge allThreads  = repo.get("tomcat.threads.config.max").gauge();

        double busyThreadsCount = busyThreads.value();
        double allThreadsCount = allThreads.value();

        System.out.println("Active thread count " + java.lang.Thread.activeCount());
        System.out.println("Busy thread count " + busyThreads.value());
        System.out.println("Max thread count " + allThreads.value());

        if (busyThreads.value() > 18){
             return new ResponseEntity(HttpStatus.SERVICE_UNAVAILABLE);
        } else {
            Thread.sleep(50);
             return new ResponseEntity<String>("Hello World!", HttpStatus.OK);
        }
    } catch (InterruptedException e) {
        e.printStackTrace();
        return new ResponseEntity(HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

  @RequestMapping("/slow")
  public String slow() {
    Random random = new Random();
    try {
        // Thread.sleep(1000 * random.nextInt(11));
        Thread.sleep(50);
        System.out.println("Active thread count " + java.lang.Thread.activeCount());
    } catch (InterruptedException e) {
        System.out.println(e.getMessage());
    }
    return "Auch";
  }

  @RequestMapping("/health")
  public String health() {
    try {
        Thread.sleep(50);
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
