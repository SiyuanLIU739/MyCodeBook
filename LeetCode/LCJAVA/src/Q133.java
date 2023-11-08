
// Definition for a Node.

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.HashMap;


class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}



public class Q133 {
    public Node cloneGraph(Node node) {
        if(node == null){
            return null;
        }

        HashSet<Node> set = new HashSet<>();

        HashMap<Node, Node> map = new HashMap<>();
        Node nnn = new Node(node.val);
        map.put(node, nnn);

        Queue<Node> q = new LinkedList<>();
        q.add(node);

        while(!q.isEmpty()){
            node = q.remove();

            if(set.contains(node)){
                continue;
            }
            
            Node newN;

            if(map.containsKey(node)){
                newN = map.get(node);
            }
            else{
                newN = new Node(node.val);
                map.put(node, newN);
            }

            for(Node n: node.neighbors){
                Node newn;

                if(map.containsKey(n)){
                    newn = map.get(n);
                }
                else{
                    newn = new Node(n.val);
                    map.put(n, newn);
                }

                newN.neighbors.add(newn);

                if(set.contains(n)){
                    continue;
                }

                q.add(n);
            }

            set.add(node);
        }

        return nnn;
    }
}
