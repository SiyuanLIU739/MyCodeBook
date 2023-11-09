import java.util.*;

class Node{
    List<Integer> tos = new LinkedList<>();
    int d = 0;

    void addTo(int to){
        this.d += 1;
        this.tos.add(to);
    }

    void delEdge(int to){
        this.d -= 1;
        this.tos.remove(to);
    }

    int getTo(){
        return this.tos.get(0);
    }

    int getD(){
        return this.d;
    }
}
public class Q310 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        Node[] graph = new Node[n];
        HashSet<Integer> remained = new HashSet<>();

        for(int i = 0; i < n; i++){
            graph[i] = new Node();
        }

        for(int i = 0; i < edges.length; i++){
            int a = edges[i][0];
            int b = edges[i][1];

            remained.add(i);
            graph[a].addTo(b);
            graph[b].addTo(a);
        }

        remained.add(n - 1);

        while(remained.size() > 2){
            Iterator<Integer> it = remained.iterator();
            ArrayList<Integer> del = new ArrayList<>();

            while(it.hasNext()){
                int a = it.next();

                if(graph[a].getD() != 1){
                    continue;
                }

                del.add(a);
            }

            for(Integer a: del){
                remained.remove(a);

                int b = graph[a].getTo();

                graph[a].delEdge(b);
                graph[b].delEdge(a);
            }
        }

        Iterator<Integer> it = remained.iterator();
        ArrayList<Integer> ans = new ArrayList<>();

        while(it.hasNext()){
            ans.add(it.next());
        }

        return ans;
    }
}
