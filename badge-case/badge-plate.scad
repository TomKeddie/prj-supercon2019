$fn=128;

corner_radius=5;
edge_offset=3;

x_size=160-72;
y_size=162-21.5;
z_battery=15.06;

z_pcb=2; // estimate
z_sao=8.4;
z_size=z_battery+z_pcb+z_sao;

post_locations=[[2, 2, 0], [86, 2, 1], [85, 58, 2], [7, 137, 3]];
post_hole_diameter=3.2;
post_pcb_height=19.05;
post_edge_offset=0.8;

%translate([0,0,post_pcb_height+z_pcb/2]) import("hadbadge2019-Edge_Cuts.dxf");

module post(direction) {
    if (direction == 0) {
        // facing NE
        translate([-post_edge_offset/2, -post_edge_offset/2]) {
            %rotate([90, 0, -45]) import("TCEHCBS-12-01/TCEHCBS-12-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 1) {
        // facing NW
        translate([+post_edge_offset/2, -post_edge_offset/2]) {
            %rotate([90, 0, +45]) import("TCEHCBS-12-01/TCEHCBS-12-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 2) {
        // facing NW
        translate([+post_edge_offset/2, +post_edge_offset/2]) {
            %rotate([90, 0, -45]) import("TCEHCBS-12-01/TCEHCBS-12-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 3) {
        // facing NW
        translate([-post_edge_offset/2, +post_edge_offset/2]) {
            %rotate([90, 0, +45]) import("TCEHCBS-12-01/TCEHCBS-12-01.stl");
            circle(d=post_hole_diameter);
        }
    }
}

//square([x_size, y_size]);
difference() {
    hull() {
        translate([-edge_offset, -edge_offset]) circle(r=corner_radius);
        translate([x_size+edge_offset, -edge_offset]) circle(r=corner_radius);
        translate([-edge_offset, y_size+edge_offset]) circle(r=corner_radius);
        translate([x_size+edge_offset, y_size+edge_offset]) circle(r=corner_radius);
    }
    
    for(location=post_locations) {
        translate([location[0], location[1]]) {
            post(location[2]);
        }
    }
}

