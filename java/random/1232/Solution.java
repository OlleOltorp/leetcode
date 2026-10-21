class Solution {
    public boolean checkStraightLine(int[][] coordinates) {

        int[] cord1 = coordinates[0];
        int[] cord2 = coordinates[1];

        int v0 = cord2[0] - cord1[0];
        int v1 = cord2[1] - cord1[1];

        for (int i = 2; i < coordinates.length; i++) {
            int[] coordinate = coordinates[i];

            int t0 = coordinate[0] - cord1[0];
            int t1 = coordinate[1] - cord1[1];

            if (((v0 * t1) - (v1 * t0)) != 0) {
                return false;
            }
        }
        return true;
    }
}