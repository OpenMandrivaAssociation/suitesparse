%global amd_version_major 3
%global amd_libname %mklibname amd
%global amd_devname %mklibname amd -d
%global amd_oldlibname %mklibname amd 2
%global amd_olddevname %mklibname amd 2 -d

%global btf_version_major 2
%global btf_libname %mklibname btf
%global btf_devname %mklibname btf -d
%global btf_oldlibname %mklibname btf 1
%global btf_olddevname %mklibname btf 1 -d

%global camd_version_major 3
%global camd_libname %mklibname camd
%global camd_devname %mklibname camd -d
%global camd_oldlibname %mklibname camd 2
%global camd_olddevname %mklibname camd 2 -d

%global ccolamd_version_major 3
%global ccolamd_libname %mklibname ccolamd
%global ccolamd_devname %mklibname ccolamd -d
%global ccolamd_oldlibname %mklibname ccolamd 2
%global ccolamd_olddevname %mklibname ccolamd 2 -d

%global cholmod_version_major 5
%global cholmod_libname %mklibname cholmod
%global cholmod_devname %mklibname cholmod d
%global cholmod_oldlibname %mklibname cholmod 3
%global cholmod_olddevname %mklibname cholmod 3 -d

%global colamd_version_major 3
%global colamd_libname %mklibname colamd
%global colamd_devname %mklibname colamd -d
%global colamd_oldlibname %mklibname colamd 2
%global colamd_olddevname %mklibname colamd 2 -d

%global csparse_version_major 4
%global csparse_libname %mklibname csparse
%global csparse_devname %mklibname csparse -d
%global csparse_oldlibname %mklibname csparse 3
%global csparse_olddevname %mklibname csparse 3 -d

%global cxsparse_version_major 4
%global cxsparse_libname %mklibname cxsparse
%global cxsparse_devname %mklibname cxsparse -d
%global cxsparse_oldlibname %mklibname cxsparse 3
%global cxsparse_olddevname %mklibname cxsparse 3 -d

%global gpuqrengine_version_major 3
%global gpuqrengine_libname %mklibname gpuqrengine
%global gpuqrengine_devname %mklibname gpuqrengine -d

%global graphblas_version_major 10
%global graphblas_libname %mklibname graphblas
%global graphblas_devname %mklibname graphblas -d

%global klu_version_major 2
%global klu_libname %mklibname klu
%global klu_devname %mklibname klu -d
%global klu_oldlibname %mklibname klu 1
%global klu_olddevname %mklibname klu 1 -d

%global klu_cholmod_version_major 2
%global klu_cholmod_libname %mklibname klu_cholmod
%global klu_cholmod_devname %mklibname klu_cholmod -d

%global lagraph_version_major 1
%global lagraph_libname %mklibname lagraph
%global lagraph_devname %mklibname lagraph -d

%global lagraphx_version_major 1
%global lagraphx_libname %mklibname lagraphx
%global lagraphx_devname %mklibname lagraphx -d

%global ldl_version_major 3
%global ldl_libname %mklibname ldl
%global ldl_devname %mklibname ldl -d
%global ldl_oldlibname %mklibname ldl 2
%global ldl_olddevname %mklibname ldl 2 -d

%global suitesparse_metis_version_major 5
%global suitesparse_metis_libname %mklibname suitesparse_metis
%global suitesparse_metis_devname %mklibname suitesparse_metis -d

%global suitesparse_mongoose_version_major 3
%global suitesparse_mongoose_libname %mklibname suitesparse_mongoose
%global suitesparse_mongoose_devname %mklibname suitesparse_mongoose -d

%global paru_version_major 1
%global paru_libname %mklibname paru
%global paru_devname %mklibname paru -d

%global rbio_version_major 4
%global rbio_libname %mklibname rbio
%global rbio_devname %mklibname rbio -d
%global rbio_oldlibname %mklibname rbio 2
%global rbio_olddevname %mklibname rbio 2 -d

%global spex_version_major 3
%global spex_libname %mklibname spex
%global spex_devname %mklibname spex -d

%define spexpython_version_major 3
%define spexpython_libname %mklibname spexpython
%define spexpython_devname %mklibname spexpython -d

%global spqr_version_major 4
%global spqr_libname %mklibname spqr
%global spqr_devname %mklibname spqr -d
%global spqr_oldlibname %mklibname spqr 1
%global spqr_olddevname %mklibname spqr 1 -d

%global suitesparseconfig_version_major 7
%global suitesparseconfig_libname %mklibname suitesparseconfig
%global suitesparseconfig_devname %mklibname suitesparseconfig -d
%global suitesparseconfig_oldlibname %mklibname suitesparseconfig 4
%global suitesparseconfig_olddevname %mklibname suitesparseconfig 4 -d

%global umfpack_version_major 6
%global umfpack_libname %mklibname umfpack
%global umfpack_devname %mklibname umfpack -d
%global umfpack_oldlibname %mklibname umfpack 5
%global umfpack_olddevname %mklibname umfpack 5 -d

%bcond gpuqrengine	0
# SuiteSparse uses a modified version of metis, so use it
%bcond system_metis	0

### CXSparse is a superset of CSparse, and the two share common header
### names, so it does not make sense to build both. CXSparse is built
### by default, but CSparse can be built instead by defining
### enable_csparse as 1 below.
%bcond csparse 	0

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 1
%else
%global arch64 0
%endif

%global blaslib flexiblas

Name:           suitesparse
Version:        7.10.2
Release:        1
Summary:        A collection of sparse matrix libraries

Group:          Development/C
License:        LGPLv2+ and GPLv2+
URL:            https://people.engr.tamu.edu/davis/suitesparse.html
Source0:        https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		suitesparse-7.7.0_fix-link.patch

BuildRequires:  cmake ninja
BuildRequires:  gmp-devel
BuildRequires:	pkgconfig(blas)
BuildRequires:	pkgconfig(lapack)
BuildRequires:	pkgconfig(%{blaslib})
%if %{with system_metis}
BuildRequires:  pkgconfig(metis)
%endif
BuildRequires:  pkgconfig(mpfr)
# openblas is still required for 64-bit suffixed versions
BuildRequires:	pkgconfig(openblas)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  hardlink

Requires:       %{amd_libname}
Requires:       %{btf_libname}
Requires:       %{camd_libname}
Requires:       %{colamd_libname}
Requires:       %{ccolamd_libname}
Requires:       %{cholmod_libname}
Requires:       %{cxsparse_libname}
Requires:       %{klu_libname}
Requires:       %{ldl_libname}
Requires:       %{spqr_libname}
Requires:       %{suitesparseconfig_libname}
Requires:       %{umfpack_libname}
Requires:       %{rbio_libname}

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.  The package includes the following libraries:
  AMD                 approximate minimum degree ordering
  BTF                 permutation to block triangular form
  CAMD                constrained approximate minimum degree ordering
  COLAMD              column approximate minimum degree ordering
  CCOLAMD             constrained column approximate minimum degree ordering
  CHOLMOD             sparse Cholesky factorization
  CSparse             a concise sparse matrix package
  CXSparse            int/long/real/complex version of CSparse
  KLU                 sparse LU factorization, BLAS-free
  GraphBLAS           graph algorithms in the language of linear algebra
  LAGraph             graph algorithms library based on GraphBLAS
  LDL                 a very concise LDL factorization package
  Mongoose            graph partitioning
  ParU                parallel unsymmetric pattern multifrontal method
  RBio                read/write sparse matrices in Rutherford/Boeing format
  SPEX                solves sparse linear systems in exact arithmetic
  SQPR                a multithread, multifrontal, rank-revealing sparse QR
                      factorization method
  UMFPACK             sparse LU factorization, with the BLAS
  SuiteSparse_config   configuration file for all the above packages.

%files

#---------------------------------------------------------------------------

%package devel
Summary:        Development headers for SuiteSparse
Group:          Development/C
Requires:       suitesparse
Provides:       suitesparse-common-devel = %{version}-%{release}
Obsoletes:      suitesparse-common-devel < 4.2.1-10

Provides:       amd-devel = %{version}-%{release}
Provides:       %{amd_devname}
Obsoletes:      %{amd_olddevname}

Provides:       btf-devel = %{version}-%{release}
Provides:       %{btf_devname}
Obsoletes:      %{btf_olddevname}

Provides:       camd-devel = %{version}-%{release}
Provides:       %{camd_devname}
Obsoletes:      %{camd_olddevname}

Provides:       ccolamd-devel = %{version}-%{release}
Provides:       %{ccolamd_devname}
Obsoletes:      %{ccolamd_olddevname}

Provides:       cholmod-devel = %{version}-%{release}
Provides:       %{cholmod_devname}
Obsoletes:      %{cholmod_olddevname}

Provides:       colamd-devel = %{version}-%{release}
Provides:       %{colamd_devname}
Obsoletes:      %{colamd_olddevname}

%if %{with csparse}
Provides:       csparse-devel = %{version}-%{release}
Provides:       %{csparse_devname}
Obsoletes:      %{csparse_olddevname}
%endif

Provides:       cxsparse-devel = %{version}-%{release}
Provides:       %{cxsparse_devname}
Obsoletes:      %{cxsparse_olddevname}

%if %{with gpuqrengine}
Provides:       gpuqrengine-devel = %{version}-%{release}
Provides:       %{gpuqrengine_devname}
%endif

Provides:       graphblas-devel = %{version}-%{release}
Provides:       %{graphblas_devname}

Provides:       klu-devel = %{version}-%{release}
Provides:       %{klu_devname}
Obsoletes:      %{klu_olddevname}

Provides:       klu_cholmod-devel = %{version}-%{release}
Provides:       %{klu_cholmod_devname}

Provides:       lagraph-devel = %{version}-%{release}
Provides:       %{lagraph_devname}

Provides:       lagraphx-devel = %{version}-%{release}
Provides:       %{lagraphx_devname}

Provides:       ldl-devel = %{version}-%{release}
Provides:       %{ldl_devname}
Obsoletes:      %{ldl_olddevname}

%if ! %{with system_metis}
Provides:       suitesparse_metis = %{version}-%{release}
Provides:       %{suitesparse_metis_devname}
%endif

Provides:       suitesparse_mongoose = %{version}-%{release}
Provides:       %{suitesparse_mongoose_devname}

Provides:       ldl-devel = %{version}-%{release}
Provides:       %{ldl_devname}
Obsoletes:      %{ldl_olddevname}

Provides:       paru-devel = %{version}-%{release}
Provides:       %{paru_devname}

Provides:       rbio-devel = %{version}-%{release}
Provides:       %{rbio_devname}

Provides:       spex-devel = %{version}-%{release}
Provides:       %{spex_devname}

Provides:       spexpython-devel = %{version}-%{release}
Provides:       %{spexpython_devname}

Provides:       spqr-devel = %{version}-%{release}
Provides:       %{spqr_devname}
Obsoletes:      %{spqr_olddevname}

Provides:       suitesparseconfig-devel = %{version}-%{release}
Provides:       %{suitesparseconfig_devname}
Obsoletes:      %{suitesparseconfig_olddevname}

Provides:       umfpack-devel = %{version}-%{release}
Provides:       %{umfpack_devname}
Obsoletes:      %{umfpack_olddevname}

%description devel
The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.

%files devel
%license Licenses
%{_includedir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/cmake/*
%{_libdir}/%{name}/pkgconfig/*
%if 0%{?arch64}
%{_includedir}/%{name}64
%dir %{_libdir}/%{name}64/
%{_libdir}/%{name}64/cmake/*
%{_libdir}/%{name}64/pkgconfig/*
%endif
%{_libdir}/lib*.so

#---------------------------------------------------------------------------

%package doc
Summary:        Documentation files for SuiteSparse
Group:          Development/C
BuildArch:      noarch

%description doc
This package contains documentation files for %{name}.

%files doc
%doc
%doc Doc/*

#---------------------------------------------------------------------------

%package -n %{suitesparseconfig_libname}
Summary:	Configuration file for SuiteSparse packages
Group:		Development/C

%description -n %{suitesparseconfig_libname}
SuiteSparse_config provides a configuration header file needed by most of 
the other packages in SuiteSparse.

%files -n %{suitesparseconfig_libname}
%{_libdir}/libsuitesparseconfig.so.%{suitesparseconfig_version_major}*
%if 0%{?arch64}
%{_libdir}/libsuitesparseconfig64.so.%{suitesparseconfig_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{amd_libname}
Summary:	Routines for permuting sparse matricies prior to factorization
Group:		Development/C

%description -n %{amd_libname}
AMD provides a set of routines for permuting sparse matricies prior to
Cholesky factorization (or LU factorization with diagonal pivoting).

%files -n %{amd_libname}
%{_libdir}/libamd.so.%{camd_version_major}*
%if 0%{?arch64}
%{_libdir}/libamd64.so.%{camd_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{btf_libname}
Summary:	Routines for permuting sparse matricies to block triangular form
Group:		Development/C

%description -n %{btf_libname}
BTF is a software package for permuting a matrix into block upper triangular
form.  It includes a maximum transversal algorithm, which finds a permutation
of a square or rectangular matrix so that it has a zero-free diagonal (if one
exists); otherwise, it finds a maximal matching which maximizes the number of
nonzeros on the diagonal.  The package also includes a method for finding the
strongly connected components of a graph.  These two methods together give the
permutation to block upper triangular form.

%files -n %{btf_libname}
%{_libdir}/libbtf.so.%{btf_version_major}*
%if 0%{?arch64}
%{_libdir}/libbtf64.so.%{btf_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{camd_libname}
Summary:	Routines for permuting sparse matricies prior to factorization
Group:		Development/C

%description -n %{camd_libname}
CAMD provides a set of routines for permuting sparse matricies prior
to factorization.

%files -n %{camd_libname}
%{_libdir}/libcamd.so.%{camd_version_major}*
%if 0%{?arch64}
%{_libdir}/libcamd64.so.%{camd_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{ccolamd_libname}
Summary:	Routines for computing column approximate minimum degree ordering
Group:		Development/C

%description -n %{ccolamd_libname}
The CCOLAMD column approximate minimum degree ordering algorithm computes
a permutation vector P such that the LU factorization of A (:,P)
tends to be sparser than that of A.  The Cholesky factorization of
(A (:,P))'*(A (:,P)) will also tend to be sparser than that of A'*A.

%files -n %{ccolamd_libname}
%{_libdir}/libccolamd.so.%{ccolamd_version_major}*
%if 0%{?arch64}
%{_libdir}/libccolamd64.so.%{ccolamd_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{cholmod_libname}
Summary:	Routines for factorizing sparse symmetric positive definite matricies
Group:		Development/C

%description -n %{cholmod_libname}
CHOLMOD is a set of routines for factorizing sparse symmetric positive
definite matrices of the form A or AA', updating/downdating a sparse
Cholesky factorization, solving linear systems, updating/downdating
the solution to the triangular system Lx=b, and many other sparse
matrix functions for both symmetric and unsymmetric matrices.  Its
supernodal Cholesky factorization relies on LAPACK and the Level-3
BLAS, and obtains a substantial fraction of the peak performance of
the BLAS.  Both real and complex matrices are supported.

%files -n %{cholmod_libname}
%{_libdir}/libcholmod.so.%{cholmod_version_major}*
%if 0%{?arch64}
%{_libdir}/libcholmod64.so.%{cholmod_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{colamd_libname}
Summary:	Routines for computing column approximate minimum degree ordering
Group:		Development/C

%description -n %{colamd_libname}
The COLAMD column approximate minimum degree ordering algorithm computes
a permutation vector P such that the LU factorization of A (:,P)
tends to be sparser than that of A.  The Cholesky factorization of
(A (:,P))'*(A (:,P)) will also tend to be sparser than that of A'*A.

%files -n %{colamd_libname}
%{_libdir}/libcolamd.so.%{colamd_version_major}*
%if 0%{?arch64}
%{_libdir}/libcolamd64.so.%{colamd_version_major}*
%endif

#---------------------------------------------------------------------------

%if %{with csparse}
%package -n %{csparse_libname}
Summary:	Direct methods for sparse linear systems
Group:		Development/C

%description -n %{csparse_libname}
CSparse is a package of direct methods for sparse linear systems written
to complement the book "Direct Methods for Sparse Linear Systems", by
Timothy A. Davis. The algorithms in CSparse have been chosen with 
five goals in mind:

(1) they must embody much of the theory behind sparse matrix algorithms,
(2) they must be either asymptotically optimal in their run time and memory
    usage or be fast in practice,
(3) they must be concise so as to be easily understood and short enough to
    print in the book,
(4) they must cover a wide spectrum of matrix operations, and
(5) they must be accurate and robust.

The focus is on direct methods; iterative methods and solvers for
eigenvalue problems are beyond the scope of this package.

%files -n %{csparse_libname}
%{_libdir}/libcsparse.so.%{csparse_version_major}
%if 0%{?arch64}
%{_libdir}/libcsparse64.so.%{csparse_version_major}
%endif
%endif

#---------------------------------------------------------------------------

%package -n %{cxsparse_libname}
Summary:	Direct methods for sparse linear systems
Group:		Development/C

%description -n %{cxsparse_libname}
CSparse is a package of direct methods for sparse linear systems written
to complement the book "Direct Methods for Sparse Linear Systems", by
Timothy A. Davis. The algorithms in CSparse have been chosen with 
five goals in mind:

(1) they must embody much of the theory behind sparse matrix algorithms,
(2) they must be either asymptotically optimal in their run time and memory
    usage or be fast in practice,
(3) they must be concise so as to be easily understood and short enough to
    print in the book,
(4) they must cover a wide spectrum of matrix operations, and
(5) they must be accurate and robust.

The focus is on direct methods; iterative methods and solvers for
eigenvalue problems are beyond the scope of this package.

CXSparse is a version of CSparse that operates on both real and complex
matrices, using either int or UF_long integers.

%files -n %{cxsparse_libname}
%{_libdir}/libcxsparse.so.%{cxsparse_version_major}*
%if 0%{?arch64}
%{_libdir}/libcxsparse64.so.%{cxsparse_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{graphblas_libname}
Summary:	A complete implementation of the GraphBLAS standard
Group:		Development/C

%description -n %{graphblas_libname}
SuiteSparse:GraphBLAS is a complete implementation of the GraphBLAS standard,
which defines a set of sparse matrix operations on an extended algebra of
semirings using an almost unlimited variety of operators and types. When
applied to sparse adjacency matrices, these algebraic operations are
equivalent to computations on graphs. GraphBLAS provides a powerful and
expressive framework for creating graph algorithms based on the elegant
mathematics of sparse matrix operations on a semiring.

%files -n %{graphblas_libname}
%{_libdir}/libgraphblas.so.%{graphblas_version_major}*
%if 0%{?arch64}
%{_libdir}/libgraphblas64.so.%{graphblas_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{klu_libname}
Summary:	Sparse LU factorization, for circuit simulation
Group:		Development/C

%description -n %{klu_libname}
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation.

%files -n %{klu_libname}
%{_libdir}/libklu.so.%{klu_version_major}*
%if 0%{?arch64}
%{_libdir}/libklu64.so.%{klu_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{klu_cholmod_libname}
Summary:        KLU sparse matrix solver with CHOLMOD support
Group:          System/Libraries

%description -n %{klu_cholmod_libname}
KLU sparse matrix solver with CHOLMOD support.

%files -n %{klu_cholmod_libname}
%{_libdir}/libklu_cholmod.so.%{klu_cholmod_version_major}*
%if 0%{?arch64}
%{_libdir}/libklu_cholmod64.so.%{klu_cholmod_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{ldl_libname}
Summary:	A consise sparse Cholesky factorization package
Group:		Development/C

%description -n %{ldl_libname}
LDL is a set of concise routines for factorizing symmetric positive-definite 
sparse matrices, with some applicability to symmetric indefinite matrices. 
Its primary purpose is to illustrate much of the basic theory of sparse matrix 
algorithms in as concise a code as possible, including an elegant new method 
of sparse symmetric factorization that computes the factorization row-by-row 
but stores it column-by-column. The entire symbolic and numeric factorization 
consists of a total of only 49 lines of code. The package is written in C,
and includes a MATLAB interface. 

%files -n %{ldl_libname}
%{_libdir}/libldl.so.%{ldl_version_major}*
%if 0%{?arch64}
%{_libdir}/libldl64.so.%{ldl_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{lagraph_libname}
Summary:	A consise sparse Cholesky factorization package
Group:		Development/C

%description -n %{lagraph_libname}
LAGraph is a library plus a test harness for collecting algorithms that
use GraphBLAS.

%files -n %{lagraph_libname}
%{_libdir}/liblagraph.so.%{lagraph_version_major}*
%{_libdir}/liblagraphx.so.%{lagraph_version_major}*
%if 0%{?arch64}
%{_libdir}/liblagraph64.so.%{lagraph_version_major}*
%{_libdir}/liblagraphx64.so.%{lagraph_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{paru_libname}
Summary:	Parallel multifrontal LU factorization algorithms
Group:		Development/C

%description -n %{paru_libname}
ParU is a set of routines for solving sparse linear system via parallel
multifrontal LU factorization algorithms. Requires OpenMP 4.5+, BLAS, CHOLMOD,
UMFPACK, AMD, COLAMD, CAMD, CCOLAMD, and METIS (in particular, the
CHOLMOD/SuiteSparse_metis variant.

%files -n %{paru_libname}
%{_libdir}/libparu.so.%{paru_version_major}*
%if 0%{?arch64}
%{_libdir}/libparu64.so.%{paru_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{rbio_libname}
Summary:	MATLAB toolbox for reading/writing sparse matrices in Rutherford/Boeing
Group:		Development/C

%description -n %{rbio_libname}
RBio - MATLAB toolbox for reading/writing sparse matrices in the
Rutherford/Boeing format, and for reading/writing problems in the UF Sparse
Matrix Collection from/to a set of files in a directory.
Version 2.0 is written in C. Older versions are in Fortran.

%files -n %{rbio_libname}
%{_libdir}/librbio.so.%{rbio_version_major}*
%if 0%{?arch64}
%{_libdir}/librbio64.so.%{rbio_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{spex_libname}
Summary:        Sparse matrix algorithms library (Spex)
Group:          System/Libraries

%description -n %{spex_libname}
Spex is a library designed for performing advanced operations on sparse matrices.

%files -n %{spex_libname}
%{_libdir}/libspex.so.%{spex_version_major}*
%if 0%{?arch64}
%{_libdir}/libspex64.so.%{spex_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{spexpython_libname}
Summary:        SPEX Python interface library
Group:          System/Libraries

%description -n %{spexpython_libname}
SPEX Python interface library.

%files -n %{spexpython_libname}
%{_libdir}/libspexpython.so.%{spexpython_version_major}*
%if 0%{?arch64}
%{_libdir}/libspexpython64.so.%{spexpython_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{spqr_libname}
Summary:	Multithreaded multifrontal sparse QR factorization
Group:		Development/C

%description -n %{spqr_libname}
SuiteSparseQR is an implementation of the multifrontal sparse QR factorization
method. Parallelism is exploited both in the BLAS and across different frontal
matrices using Intel's Threading Building Blocks, a shared-memory programming
model for modern multicore architectures. It can obtain a substantial fraction
of the theoretical peak performance of a multicore computer. The package is
written in C++ with user interfaces for MATLAB, C, and C++.

%files -n %{spqr_libname}
%{_libdir}/libspqr.so.%{spqr_version_major}*
%if 0%{?arch64}
%{_libdir}/libspqr64.so.%{spqr_version_major}*
%endif

#---------------------------------------------------------------------------

%if %{with system_metis}
%package -n %{suitesparse_metis_libname}
Summary:       A modified version of METIS
Group:         Development/C

%description -n %{suitesparse_metis_libname}
A modified version of METIS.

%files -n %{suitesparse_metis_libname}
%{_libdir}/libsuitesparse_metis.so.%{suitesparse_metis_version_major}*
%if 0%{?arch64}
%{_libdir}/libsuitesparse_metis64.so.%{metis_versisuitesparse_metis_version_majoron_major}*
%endif
%endif

#---------------------------------------------------------------------------

%package -n %{suitesparse_mongoose_libname}
Summary:       Mongoose is a graph partitioning library
Group:         Development/C

%description -n %{suitesparse_mongoose_libname}
Mongoose is a graph partitioning library. Currently, Mongoose only supports edge
partitioning, but in the future a vertex separator extension will be added.

%files -n %{suitesparse_mongoose_libname}
%{_bindir}/%{name}_mongoose
%{_libdir}/libsuitesparse_mongoose.so.%{suitesparse_mongoose_version_major}*
%if 0%{?arch64}
%{_libdir}/libsuitesparse_mongoose64.so.%{suitesparse_mongoose_version_major}*
%endif

#---------------------------------------------------------------------------

%package -n %{umfpack_libname}
Summary:	Routines for solving unsymmetric sparse linear systems
Group:		Development/C
# 5.6.1-3 is a tricky number to avoid using an epoch as old umfpack packages has a
# higher version than SuiteSparse
Provides:   %{mklibname umfpack 5.6.1} = 5.6.1-5
Obsoletes:  %{mklibname umfpack 5.6.1} < 5.6.1-5
Provides:   %{mklibname umfpack 5.5.1} = 0:5.5.1-5
Obsoletes:  %{mklibname umfpack 5.5.1} < 0:5.5.1-5
Provides:   %{mklibname umfpack 5.4.0} = 0:5.4.0-5
Obsoletes:  %{mklibname umfpack 5.4.0} < 0:5.4.0-5

%description -n %{umfpack_libname}
UMFPACK provides a set of routines for solving unsymmetric sparse
linear systems Ax=b using the Unsymmetric MultiFrontal method. It is
written in ANSI/ISO C. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack"; it is not "You Em Ef Pack".

%files -n %{umfpack_libname}
%{_libdir}/libumfpack.so.%{umfpack_version_major}*
%if 0%{?arch64}
%{_libdir}/libumfpack64.so.%{umfpack_version_major}*
%endif

#---------------------------------------------------------------------------

%prep
%autosetup -n SuiteSparse-%{version} -p1

# remove bundled
%if %{with system_metis}
  rm -r SuiteSparse_metis
  # SuiteSparse looks for SuiteSparse_metis.h specifically
  ln -s %{_includedir}/metis/metis.h include/SuiteSparse_metis.h
%endif

# collect licenses in one place to ship
mkdir Licenses
find -iname lesser.txt -o -iname lesserv3.txt -o -iname license.txt -o \
    -iname gpl.txt -o -iname GPLv2.txt -o -iname license \
    -a -not -type d | while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "./Licenses/$b/$x"
    done

# collect docs in one place to ship
mkdir Doc
find -type f -a \( -iname \*.pdf -o -iname ChangeLog -o -iname README\* -o -iname \*.txt \) |
    while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "./Doc/$b/$x"
    done

%build
export CC=gcc
export CXX=g++
##export FC=gfortran
export DEFAULT_CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lm"

for d in build%{?arch64:{,64}}
do
	if [[ "$d" =~ "64" ]]; then
 		SUITESPARSE_INCLUDEDIR_POSTFIX="suitesparse64"
		SUITESPARSE_PKGFILEDIR="%{_libdir}/suitesparse64"
		CMAKE_RELEASE_POSTFIX="64"
		BLA_VENDOR="FlexiBLAS"
		SUITESPARSE_USE_64BIT_BLAS="ON"
		BLAS_LIBRARIES="%{_libdir}/libflexiblas64.so"
		LAPACK_LIBRARIES="%{_libdir}/libflexiblas64.so"
		ARCH_CFLAGS="-DBLAS_OPENBLAS_64"
	else
		SUITESPARSE_INCLUDEDIR_POSTFIX="suitesparse"
		SUITESPARSE_PKGFILEDIR="%{_libdir}/suitesparse"
		CMAKE_RELEASE_POSTFIX=
		BLA_VENDOR="FlexiBLAS"
		SUITESPARSE_USE_64BIT_BLAS="OFF"
		BLAS_LIBRARIES="%{_libdir}/libflexiblas.so"
		LAPACK_LIBRARIES="%{_libdir}/libflexiblas.so"
		ARCH_CFLAGS=
	fi

	export CFLAGS="$DEFAULT_CFLAGS $ARCH_CFLAGS"
	%cmake \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
		-DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
		-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
		-DCOMPACT:BOOL=ON \
		-DSUITESPARSE_INCLUDEDIR_POSTFIX=$SUITESPARSE_INCLUDEDIR_POSTFIX \
		-DSUITESPARSE_PKGFILEDIR:STRING=$SUITESPARSE_PKGFILEDIR \
		-DCMAKE_RELEASE_POSTFIX:STRING=$CMAKE_RELEASE_POSTFIX \
		-DBLA_VENDOR:STRING=$BLA_VENDOR \
%if %{with system_metis}
		-DSUITESPARSE_METIS_FOUND=true \
		-DSUITESPARSE_METIS_INCLUDE_DIR=%{_includedir}/metis  \
		-DSUITESPARSE_METIS_LIBRARIES=%{_libdir}/libmetis.so \
%endif
		-GNinja

	%ninja_build
	cd ..
	mv %_vpath_builddir %_vpath_builddir-$d
done

%install
for d in build%{?arch64:{,64}}
do
	mv %_vpath_builddir-$d %_vpath_builddir
	%ninja_install -C build
	mv %_vpath_builddir %_vpath_builddir-$d
done

