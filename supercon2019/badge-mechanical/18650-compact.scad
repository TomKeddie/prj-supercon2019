// TODO - add recessed plus indicator
//      - allow multiple cells
//      - add slots for solder tabs
//
$fn=128;

battery_diameter=19.5;
battery_length=65.2;

plate_thickness=1;
wall_thickness=1.5;

side_margin=1;
spring_margin=7;
plate_margin=3;
finger_diameter=35;
terminal_width=5;

end_margin=plate_margin+spring_margin;

cavity_width=battery_diameter+side_margin;
cavity_length=battery_length+end_margin;

case_length=cavity_length+2*wall_thickness;
case_width=cavity_width+wall_thickness;
case_height=battery_diameter+plate_thickness;

mount_size=6;
mount_hole_diameter=3;

module onecell(left=0, right=0)
{
    difference()
    {
        union() {
            translate([-case_width/2, -case_length/2, 0]) cube([case_width, case_length, case_height]);
        }

        // battery cavity
        if (left != 0) {
            translate([-cavity_width/2+wall_thickness/2, -cavity_length/2, plate_thickness]) cube([cavity_width, cavity_length, battery_diameter]);
        }
        if (right != 0) {
            translate([-cavity_width/2-wall_thickness/2, -cavity_length/2, plate_thickness]) cube([cavity_width, cavity_length, battery_diameter]);
        }
        // removal opening
        translate([-case_width,0,case_height]) rotate([0,90,0]) cylinder(d=finger_diameter, h=case_width*2, $fn=64);

        // solder terminal gaps
        translate([0, -case_length/2+wall_thickness, plate_thickness]) rotate([90,0,0])cylinder(d=terminal_width, h=wall_thickness, $fn=32);
        translate([0, +case_length/2, plate_thickness]) rotate([90,0,0])cylinder(d=terminal_width, h=wall_thickness, $fn=32);
    }
}

module mount() {
    difference() {
        cube([mount_size, mount_size, case_height], center=true);
        cylinder(d=mount_hole_diameter, h=case_height, center=true);
    }
}


module twocell()
{
    translate([-case_width/2+wall_thickness/2, 0, 0]) onecell(1,0);
    translate([+case_width/2-wall_thickness/2, 0, 0]) onecell(0,1);
            
     translate([+(case_width-mount_size/2-wall_thickness/2), +(case_length/2+mount_size/2), case_height/2]) 
        mount();
     translate([-(case_width-mount_size/2-wall_thickness/2), +(case_length/2+mount_size/2), case_height/2]) 
        mount();
     translate([+(case_width-mount_size/2-wall_thickness/2), -(case_length/2+mount_size/2), case_height/2]) 
        mount();
     translate([-(case_width-mount_size/2-wall_thickness/2), -(case_length/2+mount_size/2), case_height/2]) 
        mount();
}

difference() {
    twocell();
    translate([0, 0, case_height+5/2-3]) cube([case_width*3, case_length*2, 3], center=true);
}