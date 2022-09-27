
rule all:   
    input: "mapped_reads/reads.sorted.bam",
           "mapped_reads/reads.sorted.bam.bai"

rule minimap2:
    input:
        # input files are hard-coded
        "../../data/ten_species_community_refs.fa", 
        "../../data/{sample}.fa"
    output:
        "mapped_reads/{sample}.bam"
    shell:
        "minimap2 -ax map-ont {input} | samtools view -Sb - > {output}"    

rule samtools_sort:
    input:
        "mapped_reads/{sample}.bam"
    output:
        "mapped_reads/{sample}.sorted.bam"
    shell:
        "samtools sort -T mapped_reads/{wildcards.sample} -O bam {input} > {output}"
        

rule samtools_index:
    input:
        "mapped_reads/{sample}.sorted.bam"
    output:
        "mapped_reads/{sample}.sorted.bam.bai"
    shell:
        "samtools index {input}" 

