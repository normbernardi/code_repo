
/**
 *
 * @author Norman Bernardi
 */
package WrapperTest;
public class WrapperImplement {
public static void main(String[] args) {
        WrapperShallow s1 = new WrapperShallow();
        WrapperShallow s2 = new WrapperShallow();
        System.out.println("Testing shallow objects:");
        s1.setArray(1, 2, 3);
        System.out.println("Initial array set to: " + s1.wrapperToString());
        s2.WrapperShallow(s1);
        System.out.println("Copy array set to: " + s2.wrapperToString());
        s1.setArray(4, 5, 6);
        System.out.println("Initial array set to: " + s1.wrapperToString());
        System.out.println("Copy array set to: " + s2.wrapperToString());
        if(s1.wrapperEquals(s2)) {
            System.out.println("Oops! s1 equals s2.");
        }
        else {
            System.out.println("Success! s1 does not equal s2.");
        }
        System.out.println("Testing deep objects:");
        WrapperDeep d1 = new WrapperDeep();
        WrapperDeep d2 = new WrapperDeep();
        d1.setArray(1, 2, 3);
        System.out.println("Initial array set to: " + d1.wrapperToString());
        d2.WrapperDeep(d1);
        System.out.println("Copy array set to: " + d2.wrapperToString());
        d1.setArray(4, 5, 6);
        System.out.println("Initial array set to: " + d1.wrapperToString());
        System.out.println("Copy array set to: " + d2.wrapperToString());
        if(d1.wrapperEquals(d2)) {
            System.out.println("Oops! s1 equals s2.");
        }
        else {
            System.out.println("Success! s1 does not equal s2.");
        }
    }
}
