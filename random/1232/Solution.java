class Solution {
    public boolean checkStraightLine(int[][] coordinates) {

        int[] coord1 = coordinates[0];
        int[] coord2 = coordinates[1];

        int v0 = coord2[0] - coord1[0];
        int v1 = coord2[1] - coord1[1];

        for (int i = 2; i < coordinates.length; i++) {
            int[] coordinate = coordinates[i];

            int t0 = coordinate[0] - coord1[0];
            int t1 = coordinate[1] - coord1[1];

            if (((v0 * t1) - (v1 * t0)) != 0) {
                return false;
            }
        }
        return true;
    }
}