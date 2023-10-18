import java.util.Arrays;
import java.util.HashSet;

public class Q1361 {
    public Q1361(){
        ;
    }

    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        // double-son
        if(this.doubleSon(leftChild, rightChild)){
            return false;
        }
        // solve with DFS

        HashSet<Integer> visited = new HashSet<>();
        boolean[] rooted = new boolean[leftChild.length];
        boolean[] thisVisit = new boolean[leftChild.length];
        int[] father = new int[leftChild.length];

        for(int i = 0; i < n; i++){
            father[i] = i;
        }

        for(int i = 0; i < n; i++){
            if(visited.contains(i)){
                continue;
            }

            rooted[i] = true;

            if(!this.visit(i, leftChild, rightChild, visited, rooted, thisVisit, father)){
                return false;
            }
            else{
                if(visited.size() == n){
                    return this.checkOneTree(father);
                }
            }
        }

        return false;
    }

    public boolean checkOneTree(int[] father){
        int f = this.getFather(father, 0);
        for(int i = 1; i < father.length; i++){
            if(this.getFather(father, i) != f){
                return false;
            }
        }
        return true;
    }

    public int getFather(int[] father, int root){
        if(father[root] == root){
            return root;
        }
        father[root] = getFather(father, father[root]);
        return father[root];
    }

    public boolean doubleSon(int[] left, int[] right){
        int[] sons = new int[left.length * 2];
        
        int n = -1;
        for(int i: left){
            n++;
            sons[n] = i;
        }
        for(int i: right){
            n++;
            sons[n] = i;
        }

        Arrays.sort(sons);

        for(int i = 1; i <= n; i++){
            if(sons[i] == sons[i - 1]){
                if(sons[i] == -1){
                    continue;
                }
                return true;
            }
        }
        return false;
    }

    public boolean visit(int root, int[] leftChildren, int[] rightChildren, HashSet<Integer> visited, boolean[] rooted, boolean[] thisVisit, int[] father){
        // not a valid node
        if(root == -1){
            return true;
        }

        // circle
        if(thisVisit[root]){
            return false;
        }

        // visit the current node
        thisVisit[root] = true;

        // don't search a searched sub-tree
        if(rooted[root]){
            if(visited.contains(root)){
                return true;
            }
        }

        visited.add(root);

        if(leftChildren[root] != -1){
            father[leftChildren[root]] = root;
        }
        if(rightChildren[root] != -1){
            father[rightChildren[root]] = root;
        }

        boolean left = visit(leftChildren[root], leftChildren, rightChildren, visited, rooted, thisVisit, father);
        boolean right = visit(rightChildren[root], leftChildren, rightChildren, visited, rooted, thisVisit, father);

        thisVisit[root] = false;
        return left&right;
    }

    public static void main(String[] args) {
        int n = 2;
        int[] left = {1,-1,3,-1};
        int[] right = {2,-1,-1,-1};
        Q1361 ans = new Q1361();
        System.out.println(ans.validateBinaryTreeNodes(n, left, right));
    }
}
