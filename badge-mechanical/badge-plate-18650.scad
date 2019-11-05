
$fn=128;

corner_radius=5;
edge_offset=8;

x_size=160-72;
y_size=162-21.5;

z_pcb=2; // estimate

post_locations=[[2, 2, 0], [86, 2, 1], [85, 58, 2], [7, 137, 3]];
post_hole_diameter=3.2;
post_pcb_height=22.23;
post_edge_offset=0.8;

y_battery_opening=39.5;
x_battery_opening=75.25;

y_battery_position=19+46/2;
x_battery_position=x_size/2-8;

z_battery_holder=19;
battery_holder_hole_diameter=3.2;
battery_holder_wall_thickness=1.5;
battery_holder_hole_offset=3;

%translate([0,0,post_pcb_height+z_pcb/2]) import("hadbadge2019-Edge_Cuts.dxf");
%translate([0,0,post_pcb_height+z_pcb/2]) import("hadbadge2019-B_Cu.dxf");


module post(direction) {
    if (direction == 0) {
        // facing NE
        translate([-post_edge_offset/2, -post_edge_offset/2]) {
            %rotate([90, 0, -45]) import("TCEHCBS-14-01/TCEHCBS-14-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 1) {
        // facing NW
        translate([+post_edge_offset/2, -post_edge_offset/2]) {
            %rotate([90, 0, +45]) import("TCEHCBS-14-01/TCEHCBS-14-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 2) {
        // facing NW
        translate([+post_edge_offset/2, +post_edge_offset/2]) {
            %rotate([90, 0, -45]) import("TCEHCBS-14-01/TCEHCBS-14-01.stl");
            circle(d=post_hole_diameter);
        }
    } else if (direction == 3) {
        // facing NW
        translate([-post_edge_offset/2, +post_edge_offset/2]) {
            %rotate([90, 0, +45]) import("TCEHCBS-14-01/TCEHCBS-14-01.stl");
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
    
    // posts
    for(location=post_locations) {
        translate([location[0], location[1]]) {
            post(location[2]);
        }
    }
    
    
    // battery opening
    translate([x_battery_position, y_battery_position]) {
        // model
        translate([0, 0, z_battery_holder]) %rotate([180, 0, 90]) import("18650-compact.stl");
        // opening
        square([x_battery_opening, y_battery_opening], center=true);
        // holes
        translate([+(x_battery_opening/2+battery_holder_hole_offset+battery_holder_wall_thickness), +(y_battery_opening/2-battery_holder_wall_thickness)])
            circle(d=battery_holder_hole_diameter);
        translate([-(x_battery_opening/2+battery_holder_hole_offset+battery_holder_wall_thickness), +(y_battery_opening/2-battery_holder_wall_thickness)])
            circle(d=battery_holder_hole_diameter);
        translate([+(x_battery_opening/2+battery_holder_hole_offset+battery_holder_wall_thickness), -(y_battery_opening/2-battery_holder_wall_thickness)])
            circle(d=battery_holder_hole_diameter);
        translate([-(x_battery_opening/2+battery_holder_hole_offset+battery_holder_wall_thickness), -(y_battery_opening/2-battery_holder_wall_thickness)])
            circle(d=battery_holder_hole_diameter);
    }
}

