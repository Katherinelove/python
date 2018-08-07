aliens=[]
for i in range(10):
    new_alien={"color":"green","zengshuai":"katehreine","flower":"pink"}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("......")
print("total of alien is=",len(aliens))
for alien in aliens[-3:]:
    if alien["color"]=="green":
        alien["color"]="yellow"
        alien["zengshuai"]="kate"
        alien["flower"]="fsdaf"
for alien in aliens:
    print(alien)
print("total of alien is=",len(aliens))