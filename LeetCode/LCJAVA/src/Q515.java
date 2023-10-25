class TreeNodeLayer{
    int layer;
    TreeNode node;

    TreeNodeLayer(TreeNode node, int layer){
        this.layer = layer;
        this.node = node;
    }
}
class Solution {


    public List<Integer> largestValues(TreeNode root) {
        HashMap<Integer, Integer> ans = new HashMap<>();
        ArrayList<Integer> ansList = new ArrayList<>();

        LinkedList<TreeNodeLayer> q = new LinkedList<>();
        if(root != null){
            q.add(new TreeNodeLayer(root, 0));
        }


        int maxLayer = -1;

        while(!q.isEmpty()){
            TreeNodeLayer rt = q.getFirst();
            q.removeFirst();
            int layer = rt.layer;
            TreeNode node = rt.node;
            int val;
            maxLayer = max(maxLayer, layer);

            if(ans.containsKey(layer)){
                val = ans.get(layer);
            }
            else{
                val = -2147483648;
            }

            val = max(val, rt.node.val);
            ans.put(layer, val);

            if(node.left != null){
                q.addLast(new TreeNodeLayer(node.left, layer + 1));
            }
            if(node.right != null){
                q.addLast(new TreeNodeLayer(node.right, layer + 1));
            }
        }

        for(int i = 0; i <= maxLayer; i++){
            ansList.add(i, ans.get(i));
        }

        return ansList;
    }

    public int max(int a, int b){
        if(a > b){
            return a;
        }
        return b;
    }
}